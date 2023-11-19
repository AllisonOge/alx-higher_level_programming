#!/usr/bin/python3
"""
module for database filtering using SQLAlchemy
"""
import sys
from sqlalchemy.orm import Session
from model_state import Base, State

from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query_results = session.query(State)\
                           .filter(State.name.ilike("%a%"))\
                           .order_by(State.id).all()
    for state in query_results:
        print("{}: {}".format(state.id, state.name))

    session.close()
