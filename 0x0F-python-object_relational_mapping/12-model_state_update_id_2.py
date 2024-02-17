#!/usr/bin/python3
"""This change the name of the State where id = 2 to New Mexico."""
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
    state_update = session.query(State).filter(State.id == 2).first()
    if state_update:
        state_update.name = "New Mexico"
        session.commit()
    session.close()
