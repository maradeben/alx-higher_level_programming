#!/usr/bin/python3
""" show all State with name passed as argument """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name==argv[4]).order_by(State.id).first()

    if not state:
        print("Not found")
    else:
        print(state.id)
    session.close()
