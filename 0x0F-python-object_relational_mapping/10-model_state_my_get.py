#!/usr/bin/python3
"""This prints the State object with the name passed as argument from database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).\
        filter(State.name == argv[4]).order_by(State.id).all()
    if states:
        print("{}".format(states[0].id))
    else:
        print("Not found")
    session.close()
