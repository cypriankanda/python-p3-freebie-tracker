#!/usr/bin/env python3

# Script goes here!
from models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connect to SQLite DB
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop and recreate all tables (optional: wipe database before reseeding)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create sample companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)

# Create sample devs
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# Create sample freebies
f1 = Freebie(item_name="T-shirt", value=10, company=google, dev=alice)
f2 = Freebie(item_name="Mug", value=5, company=google, dev=bob)
f3 = Freebie(item_name="Sticker", value=1, company=microsoft, dev=alice)

# Add and commit
session.add_all([google, microsoft, alice, bob, f1, f2, f3])
session.commit()
