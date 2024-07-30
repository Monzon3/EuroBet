from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData

load_dotenv()

sql_username = os.getenv("MYSQL_USER")
sql_password = os.getenv("MYSQL_PASSWORD")
sql_database = os.getenv("MYSQL_DATABASE")

engine = create_engine(f"mysql+pymysql://{sql_username}:{sql_password}@db:3306/{sql_database}")
meta = MetaData()
conn = engine.connect()