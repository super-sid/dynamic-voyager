from fastapi import FastAPI, Model
from typing import List

class Post(Model):
    id = int
    title = str
    content = str
    author = str

class SearchResult(Model):
    id = int
    title = str
    content = str
    author = str

posts = List[Post]()

@app.get("/posts")
async def read_posts():
    return posts

@app.post("/posts/create")
async def create_post(title: str, content: str, author: str):
    post = Post(title=title, content=content, author=author)
    posts.append(post)
    return {"message": "Post created"}

@app.get("/posts/{id}")
async def read_post(id: int):
    return posts[id]

@app.put("/posts/{id}")
async def update_post(id: int, title: str, content: str, author: str):
    post = Post.from_dict({"title": title, "content": content, "author": author})
    posts[id] = post
    return {"message": "Post updated"}

@app.delete("/posts/{id}")
async def delete_post(id: int):
    del posts[id]
    return {"message": "Post deleted"}