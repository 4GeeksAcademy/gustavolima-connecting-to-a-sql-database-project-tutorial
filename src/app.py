import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
con = engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
# Leer el contenido del archivo create.sql
with open('./src/sql/create.sql') as file:
    create_sql = file.read()

# Delete Tables if they already exist
con.execute('DROP TABLE IF EXISTS publishers, authors, books, book_authors, epub CASCADE')

# Execute the SQL code
con.execute(create_sql)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
# Read insert.sql content
with open('./src/sql/insert.sql') as file:
    insert_sql = file.read()

# Execute the task
con.execute(insert_sql)

# 4) Use pandas to print one of the tables as dataframes using read_sql function
# Read the "books" Table
df = pd.read_sql('SELECT * FROM publishers', con=engine)

# Print the DataFrame
print(df.to_string(index=False))
