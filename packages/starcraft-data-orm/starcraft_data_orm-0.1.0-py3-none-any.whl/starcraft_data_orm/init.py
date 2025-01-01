from sqlalchemy import create_engine

from starcraft_data_orm.warehouse.datapack.unit_type import unit_type
from starcraft_data_orm.warehouse.datapack.ability import ability

from starcraft_data_orm.warehouse.replay.map import map
from starcraft_data_orm.warehouse.replay.user import user
from starcraft_data_orm.warehouse.replay.info import info
from starcraft_data_orm.warehouse.replay.player import player
from starcraft_data_orm.warehouse.replay.object import object

from starcraft_data_orm.warehouse.events.basic_command_event import basic_command_event
from starcraft_data_orm.warehouse.events.chat_event import chat_event
from starcraft_data_orm.warehouse.events.player_leave_event import player_leave_event
from starcraft_data_orm.warehouse.events.player_stats_event import player_stats_event
from starcraft_data_orm.warehouse.events.unit_born_event import unit_born_event
from starcraft_data_orm.warehouse.events.unit_died_event import unit_died_event
from starcraft_data_orm.warehouse.events.unit_done_event import unit_done_event
from starcraft_data_orm.warehouse.events.unit_init_event import unit_init_event
from starcraft_data_orm.warehouse.events.upgrade_complete_event import upgrade_complete_event

from starcraft_data_orm.config import engine
from starcraft_data_orm.base import Base

import asyncio
from sqlalchemy.sql import text

def init_db():
    """Asynchronously initialize the starcraft_data_orm schema."""

    with engine.begin() as conn:
        # Create schemas if they do not exist
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS datapack;"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS events;"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS replay;"))

    # Create all tables
    Base.metadata.create_all(bind=engine)

    engine.dispose()

