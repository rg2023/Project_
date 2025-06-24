from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from app.utils.secret import get_secret

def insert_data(name, value, project_id):
    connector = Connector()
    db_user = get_secret("db-user", project_id)
    db_password = get_secret("db-password", project_id)
    db_name = get_secret("db-name", project_id)
    connection_name = get_secret("db-host", project_id) 
    def getconn():
       return connector.connect(
        connection_name,
        "pymysql", 
        user=db_user,
        password=db_password,
        db=db_name,
    )
    engine = sqlalchemy.create_engine(
        "mysql+pymysql://",  
        creator=getconn,
    )
    
    with engine.connect() as conn:
        conn.execute(sqlalchemy.text(
            "INSERT INTO my_table (name, value) VALUES (:name, :value)"
        ), {"name": name, "value": value})