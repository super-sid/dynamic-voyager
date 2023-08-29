from fastapi import FastAPI, Route, response
from .models import Post

app = FastAPI()

@app.get("/")
def read_index():
    return {"message": "Welcome to my blog"}

@app.post("/create-post")
def create_post(title: str, content: str):
    post = Post(title, content)
    app.database.add(post)
    return {"message": "Post created successfully"}

@app.get("/posts/{id}")
def read_post(id: int):
    post = app.database.get(id)
    if post is None:
        return {"message": "Post not found"}, 404
    return post.to_dict()

@app.put("/posts/{id}")
def update_post(id: int, title: str, content: str):
    post = app.database.get(id)
    if post is None:
        return {"message": "Post not found"}, 404
    post.title = title
    post.content = content
    app.database.update(post)
    return {"message": "Post updated successfully"}

@app.delete("/posts/{id}")
def delete_post(id: int):
    post = app.database.get(id)
    if post is None:
        return {"message": "Post not found"}, 404
    app.database.delete(post)
    return {"message": "Post deleted successfully"}