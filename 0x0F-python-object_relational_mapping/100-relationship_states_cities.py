#!/usr/bin/python3
""" create State “California” with City “San Francisco” from database
    hbtn_0e_100_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    the_state = State(name="California")
    the_city = City(name="San Francisco")
    the_state.cities.append(the_city)
    session.add_all([the_city, the_state])
    session.commit()
    session.close()
