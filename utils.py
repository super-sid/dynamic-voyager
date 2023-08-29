from fastapi import FastAPI, Security, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello, World!": "From FastAPI"}

@app.post("/login")
async def login(username: str, password: str):
    # Implement authentication logic here
    return {"logged_in": True}

@app.get("/protected")
async def protected():
    # Check if user is logged in
    if not logged_in:
        return {"error": "You must be logged in to access this page"}
    return {"Hello, Logged In User!": "From FastAPI"}

@app.post("/logout")
async def logout():
    # Implement logout logic here
    return {"logged_in": False}