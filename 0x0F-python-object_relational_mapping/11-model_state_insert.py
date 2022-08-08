#!/usr/bin/python3
"""
Script that lists all State objects from the
hbtn_0e_6_usa database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_State = State(name="Louisiana")
    session.add(new_State)
    session.commit()
    print(new_State.id)

    session.close()
