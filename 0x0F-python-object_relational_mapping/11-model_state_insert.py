#!/usr/bin/python3
"""This to adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(db_username, db_password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_add = State(name="Louisiana")
    session.add(new_add)
    session.commit()
    print(new_add.id)
    session.close()
