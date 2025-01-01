from factory import Sequence, Faker, Iterator
from factory.alchemy import SQLAlchemyModelFactory

from starcraft_data_orm.config import SessionLocal
from starcraft_data_orm.warehouse.unit_type import unit_type

class UnitTypeFactory(SQLAlchemyModelFactory):
    class Meta:
        model = unit_type
        sqlalchemy_session = SessionLocal

    release_string = "1.0.0"
    id = Sequence(lambda n: n)
    str_id = Faker("word")
    name = Faker("name")
    title = Faker("name")
    race = Iterator(["Terran", "Protoss", "Zerg"])
    minerals = Faker("random_int", min=50, max=500)
    vespene = Faker("random_int", min=0, max=500)
    supply = Faker("random_int", min=0, max=10)
    is_building = Faker("boolean")
    is_army   = Faker("boolean")
    is_worker = Faker("boolean")
