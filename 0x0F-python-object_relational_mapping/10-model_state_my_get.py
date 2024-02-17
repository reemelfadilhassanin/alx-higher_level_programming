#!/usr/bin/python3
"""This prints the State object with the name passed as argument from database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State):
        if (state.name == argv[4]):

            print(state.id)
            break
    else:
        print("Not found")
