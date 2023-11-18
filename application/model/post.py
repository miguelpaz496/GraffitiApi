from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, DateTime, TIMESTAMP, Float
from sqlalchemy import text
from datetime import datetime, timezone
from application.config.db import engine, meta_data

posts = Table("post", meta_data, 
                Column("id", Integer, primary_key=True),
                Column("name", String(50), nullable=False),
                Column("description", String(50), nullable=False),
                Column("latitude", Float, nullable=False),
                Column("longitude", Float, nullable=False),     
                Column("date_created", Date , server_default=text("CURRENT_TIMESTAMP") ,nullable=False ),
                Column("date_updated", TIMESTAMP , server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP") , nullable=False))

meta_data.create_all(engine)
