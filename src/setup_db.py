from sqlalchemy import *

db = create_engine('mysql+pymysql://python_user@localhost:3306/spending-tracker')


metadata = MetaData()

receipts = Table('receipts', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('date', Date, nullable=False),
                 Column('shop', String(100), nullable=False))

items = Table('items', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('name', String(200), nullable=False),
              Column('category', String(100), nullable=False),
              Column('latest_price', Float, nullable=True))

units = Table('units', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('name', String(100), nullable=False),
              Column('unit_type', String(10), nullable=True),
              Column('container_size', Integer, nullable=True),
              Column('container_type', String(50), nullable=True))

lines = Table('lines', metadata,
              Column('receipt_id', Integer, ForeignKey('receipts.id'), primary_key=True),
              Column('item_id', Integer, ForeignKey('items.id'), primary_key=True),
              Column('unit_id', Integer, ForeignKey('units.id'), nullable=True),
              Column('price', Float, nullable=False),
              Column('amount', Integer, nullable=False))


metadata.create_all(db)
