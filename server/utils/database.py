from google.cloud.sql.connector import Connector
import sqlalchemy

def insert_data(name, value):
    connector = Connector()
    def getconn():
        return connector.connect(
            "YOUR_CONNECTION_NAME", 
            "pg8000",
            user="USERNAME",
            password="PASSWORD",
            db="db"
        )
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    with pool.connect() as conn:
        conn.execute(sqlalchemy.text(
            "INSERT INTO my_table (name, value) VALUES (:name, :value)"
        ), {"name": name, "value": value})
