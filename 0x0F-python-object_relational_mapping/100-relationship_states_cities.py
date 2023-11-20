#!/usr/bin/python3
"""
module for creating related objects using SQLAlchemy
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import Session

from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name="California")
    session.add(state)
    session.commit()
    session.add(City(name="San Francisco", state_id=state.id))
    session.commit()
    session.close()
