from fastapi import Depends,status,HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import boto3
import json

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
# SECRET_KEY
#Algorithm
#expiration time


#for geting url from aws secretsmanager
client = boto3.client('secretsmanager')

responce = client.get_secret_value(
    SecretId='fastapi_secret3',
)
#converts secret id to dict called secretdict
secretDict = json.loads(responce['SecretString'])



SECRET_KEY = secretDict['secret']
ALGORITHM = secretDict['alg']
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_acess__token(token: str, credentials_exception):


    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session =  Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_acess__token(token, credentials_exception)

    user = db. query(models.User).filter(models.User.id == token.id).first()
    
    return user