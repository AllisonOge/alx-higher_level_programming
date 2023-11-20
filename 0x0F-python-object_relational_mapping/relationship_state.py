#!/usr/bin/python3
"""
module for state model definition using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ORM for states relational table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state",
                          cascade="all, delete, delete-orphan")  # many-to-one
