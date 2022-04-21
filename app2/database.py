
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import boto3
import json

#for geting url from aws secretsmanager
client = boto3.client('secretsmanager')

responce = client.get_secret_value(
    SecretId='aws_database_connection',
)
#converts secret id to dict called secretdict
secretDict = json.loads(responce['SecretString'])

#database connection on aws
SQLALCHEMY_DATABASE_URL = secretDict['URL']                                                 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
     db = SessionLocal()
     try:
         yield db
     finally:
         db.close()


# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi', user='postgres', password='admin', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
   