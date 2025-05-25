#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie  # make sure Freebie is imported!

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Optional: preload some data into variables for testing
    companies = session.query(Company).all()
    devs = session.query(Dev).all()
    freebies = session.query(Freebie).all()

    # Start debugging session
    import ipdb; ipdb.set_trace()
