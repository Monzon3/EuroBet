from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData

load_dotenv()
sql_username = os.getenv("SQL_ADMIN_USERNAME")
sql_password = os.getenv("SQL_ADMIN_PASSWORD")
engine = create_engine(f"mysql+pymysql://{sql_username}:{sql_password}@db:3306/PorraEuro")
meta = MetaData()
conn = engine.connect()