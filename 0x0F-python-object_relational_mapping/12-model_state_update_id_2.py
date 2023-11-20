#!/usr/bin/python3
"""
module for updating a record using SQLAlchemy
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
    # updating requires the following steps
    # 1. quering the record needed
    # 2. modify the attributes of the retrived object
    # 3. commit the changes to the database
    state2update = session.query(State).filter_by(id=2).first()

    if state2update:  # check if record exists
        state2update.name = "New Mexico"

        session.commit()
    session.close()
