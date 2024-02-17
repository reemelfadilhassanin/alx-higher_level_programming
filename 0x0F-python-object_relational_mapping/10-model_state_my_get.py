#!/usr/bin/python3
"""This prints the State object with the name passed as argument from database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_state import State
from sys import argv

if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(db_username, db_password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    db_session = Session()

    first_state = db_session.query(State).filter(
        State.name == state_name).first()

    if first_state:
        print(first_state.id)
    else:
        print("Not found")

    db_session.close()
