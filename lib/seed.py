#!/usr/bin/env python3

# Script goes here!
# Create instances
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Create the engine and session
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables in the database
Base.metadata.create_all(engine)

# Create sample data using CRUD statements
company1 = Company(name='Company A', founding_year=2000)
company2 = Company(name='Company B', founding_year=2010)
dev1 = Dev(name='Dev 1')
dev2 = Dev(name='Dev 2')
session.add_all([company1, company2, dev1, dev2])
session.commit()

company1.give_freebie(dev1, 'T-shirt', 10)
company1.give_freebie(dev2, 'Stickers', 5)

# Print the details of the freebies
for freebie in session.query(Freebie).all():
    print(freebie.print_details())


