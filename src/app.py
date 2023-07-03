import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv('.env')
db_url = os.getenv('DATABASE_URL')

# 1) Connect to the database here using the SQLAlchemy's create_engine function
engine = create_engine(db_url)
con = engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
with open('src/sql/create.sql') as file:
    create = file.read()

try:
    con.execute(create)
    print("Tables created successfully.")
except Exception as e:
    print("Error occurred while creating tables:", str(e))

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

with open('src/sql/insert.sql') as file:
    insert = file.read()

try:
    con.execute(insert)
    print("Data inserted successfully.")
except Exception as e:
    print("Error occurred while inserting data:", str(e))


# 4) Use pandas to print one of the tables as dataframes using read_sql function

df = pd.read_sql('SELECT * FROM publishers', engine)
print(df)

engine.dispose()