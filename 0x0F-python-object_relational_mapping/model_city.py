#!/usr/bin/python3
"""
module for City model definition
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ORM for cities relational table"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")  # one-to-many

State.cities = relationship("City", back_populates="state")  # many-to-one
