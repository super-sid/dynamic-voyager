from fastapi import FastAPI, APIRouter, Depends
from fastapi.templating import Template
from .models import Post
from .routes import post_route

app = FastAPI()

# Create a router for the posts
router = APIRouter()

@router.get("/posts")
def get_posts():
    return Post.query.all()

@router.post("/posts/<int:post_id>")
def create_post(post_id: int, content: str):
    post = Post.create(content=content)
    return post

@router.get("/posts/<int:post_id>")
def get_post(post_id: int):
    post = Post.find_by_id(post_id)
    if post is None:
        raise ValueError("Post not found")
    return post

@router.put("/posts/<int:post_id>")
def update_post(post_id: int, content: str):
    post = Post.find_by_id(post_id)
    if post is None:
        raise ValueError("Post not found")
    post.content = content
    return post

@router.delete("/posts/<int:post_id>")
def delete_post(post_id: int):
    Post.delete_by_id(post_id)
    return {"message": "Post deleted"}

# Add the router to the application
app.include_router(router)

# Add a template for the posts list
template = Template("templates/list.html")

@app.get("/posts/")
async def get_posts():
    return {
        "posts": [
            template.render(post=post)
            for post in Post.query.all()
        ]
    }
<!DOCTYPE html>
<html>
<head>
    <title>Posts</title>
</head>
<body>
    <h1>Posts</h1>
    <ul>
        {% for post in posts %}
            <li>{{ post.content }}</li>
        {% endfor %}
    </ul>
</body>
</html>