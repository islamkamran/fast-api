from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# make an instance
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # completely optional
    rating: Optional[int] = None

# @ is for decorator
@app.get("/")
def root():
    return {"Hello": "World is a great place for living and enjoying"}

@app.get("/getposts")
def get_posts():
    return {"Data":"This is your post"}

@app.post("/createposts")
def create_post(new_post: Post):
    # print(new_post.rating)
    new_post.dict()
    return {"data": new_post}



# to run
# uvicorn NameOfTheFile:NameOfTheInstance in command line