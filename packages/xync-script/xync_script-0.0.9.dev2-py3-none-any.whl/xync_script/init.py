from pg_channel import plsql, Act
from tortoise.backends.asyncpg import AsyncpgDBClient
from x_model import init_db
from uvloop import run
from xync_schema import models
from xync_schema.enums import exs
from xync_schema.models import Ex, TestEx, ExAction

from xync_script.loader import dsn


async def main():
    cn = await init_db(dsn, models, True)

    await Ex.bulk_create(
        (
            Ex(name=n, type_=val[0], logo=val[1], host=val[2], host_p2p=val[3], url_login=val[4])
            for n, val in exs.items()
        ),
        update_fields=["host", "host_p2p", "logo", "url_login"],
        on_conflict=["name", "type_"],
    )
    texs = [TestEx(ex=ex, action=act) for act in ExAction for ex in await Ex.exclude(logo="")]
    await TestEx.bulk_create(texs, ignore_conflicts=True)
    print("Exs&TestExs filled DONE")

    await set_triggers(cn)
    print("Triggers set DONE")
    await cn.close()


async def set_triggers(cn: AsyncpgDBClient):
    # plsql("dep", Act.NEW+Act.UPD, {"stts": ("is_active",), "_prof": ["apr", "max_limit", "fee"]})
    ad = plsql("ad", Act.NEW + Act.UPD + Act.DEL, {"prof": ["price", "maxFiat", "minFiat"], "stts": ("status",)})
    order = plsql("order", Act.NEW + Act.UPD + Act.DEL, {"stts": ("status",)})
    msg = plsql("msg", Act.NEW)
    await cn.execute_script(ad)
    await cn.execute_script(order)
    await cn.execute_script(msg)


if __name__ == "__main__":
    run(main())
