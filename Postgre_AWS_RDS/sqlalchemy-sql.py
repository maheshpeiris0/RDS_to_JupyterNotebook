import pandas as pd
from sqlalchemy import create_engine

# Replace the following variables with your actual details
username = 'postgres'
password = ''
host = ''
port = '5432'
database = 'class_db'

# Create the connection URL
connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

# Create the engine
engine = create_engine(connection_url)

# Query and load into DataFrame
with engine.connect() as connection:
    df = pd.read_sql("SELECT * FROM apple_table", con=connection)

print(df)
