from sqlalchemy import *
from tables import get_tables

db = create_engine('mysql+pymysql://python_user@localhost:3306/spending-tracker')

metadata = MetaData(bind=db)
tables = get_tables(metadata)
metadata.create_all()

con = db.connect()
insert = tables["receipts"].insert().values(date='2021-05-18', shop='Testco')
con.execute(insert)
