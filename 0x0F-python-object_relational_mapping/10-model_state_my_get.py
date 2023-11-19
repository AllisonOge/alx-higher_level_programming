#!/usr/bin/python3
"""
module for quering database for a record usign SQLAlchemy
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
    query_result = session.query(State)\
                          .filter_by(name = sys.argv[4])\
                          .order_by(State.id).first()
    if not query_result:
        print("Not found")
    else:
        print("{}".format(query_result.id))
    session.close()
