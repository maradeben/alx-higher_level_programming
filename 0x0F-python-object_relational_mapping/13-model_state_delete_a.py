#!/usr/bin/python3
""" delete states with a in their names """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ =="__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).filter(State.name.like('%a%'))

    if q is not None:
        for state in q:
            session.delete(state)

    session.commit()
    session.close()
