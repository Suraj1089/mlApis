from fastapi import FastAPI
from .database import Base, engine
from .routers import blog, user


Base.metadata.create_all(bind=engine)


app = FastAPI()


# create instance of CryptContext to hash and verify passwords

app.include_router(blog.router)
app.include_router(user.router)
