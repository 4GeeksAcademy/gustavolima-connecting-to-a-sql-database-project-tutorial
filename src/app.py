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

# Eliminar las tablas si existen
con.execute('DROP TABLE IF EXISTS publishers, authors, books, book_authors, epub CASCADE')

# Ejecutar las sentencias SQL para crear las tablas
con.execute(create_sql)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
# Leer el contenido del archivo insert.sql
with open('./src/sql/insert.sql') as file:
    insert_sql = file.read()

# Ejecutar las sentencias SQL para insertar los datos
con.execute(insert_sql)

# 4) Use pandas to print one of the tables as dataframes using read_sql function
# Leer la tabla "books" como un DataFrame
df = pd.read_sql('SELECT * FROM publishers', con=engine)

# Imprimir el DataFrame sin el índice
print(df.to_string(index=False))