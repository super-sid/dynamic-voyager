from fastapi import FastAPI, APIRouter, Depends
from fastapi.templating import Template
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

# Define a router for our blog posts
blog_router = APIRouter()

@blog_router.get("/posts")
def read_all_posts():
    return JSONResponse(content={"posts": [
        {"id": 1, "title": "Post 1", "content": "This is the content of post 1."},
        {"id": 2, "title": "Post 2", "content": "This is the content of post 2."},
        {"id": 3, "title": "Post 3", "content": "This is the content of post 3."}
    ]})

@blog_router.get("/posts/{id}")
def read_post(id: int):
    return JSONResponse(content={"post": {"id": id, "title": "Post {}".format(id), "content": "This is the content of post {}.".format(id)}})

@blog_router.post("/posts")
def create_post(post: dict):
    return JSONResponse(content={"id": post["id"], "title": post["title"], "content": post["content"]})

@app.get("/")
def read_index():
    return Template("index", {"posts": [p for p in blog_router.get_all()]})

@app.get("/posts/{id}")
def read_post(id: int):
    post = blog_router.get(id)
    if post is None:
        return JSONResponse(content={"message": "Post not found."}, status_code=404)
    return Template("post", {"post": post})