from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/post")
def get_posts():
    return {"data": "this is your post"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "this is my first post"}