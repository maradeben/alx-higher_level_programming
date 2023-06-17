#!/usr/bin/python3
""" insert a new state """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ =="__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).filter(State.id==2).first()
    q.name = 'New Mexico'
    session.commit()
    session.close()
