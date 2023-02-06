from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/post")
def get_posts():
    return {"data": "this is your post"}