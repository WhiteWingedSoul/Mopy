from table import Table
from seed.rand_int_seed import RandIntSeed
from seed.pk_int_seed import PkIntSeed
from seed.enum_seed import EnumSeed 
from seed.rand_string_seed import RandStrSeed
from seed.rand_boolean_seed import RandBoolSeed
from seed.rand_date_seed import RandDateSeed
from seed.rand_date_time_seed import RandDateTimeSeed

if __name__ == "__main__":

    users = Table(
        "users",
        id=PkIntSeed(),
        age=RandIntSeed(min=0, max=100),
        name=RandStrSeed(size=5),
        birth=RandDateSeed()
    )

    items = Table(
        "items",
        id=PkIntSeed(),
        price=RandIntSeed(min=0, max=1000),
        user_id=users("id"),
        user_name=users("name"),
        type=EnumSeed(["ONE", "TWO", "THERE"]),
        is_active=RandBoolSeed(),
        created_dt=RandDateTimeSeed()
    )

    users.create(7).show_sql()
    items.create(5).show_sql()