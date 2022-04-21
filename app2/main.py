from email.quoprimime import body_check
from fastapi import FastAPI
from app2 import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware



# used for creating tables before alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



@app.get("/")                            # Path operation/ route   / = route url (og)
def root():
    return {"message": "Hello world"}    # Data that gets send back          

''' adding --reload makes your server reload everytime the code is changed 
    add it in start up when runing original code of uvicorn main:app '''

#  CRUD - Create Read Update Delete
    # Create /posts .post
    # Read individual - /posts/:id all - /posts    .get
    #   Update /posts  .put
    # Delete /posts/:id .delete

# new path operation for sending user data to api

