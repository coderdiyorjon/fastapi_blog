from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates= Jinja2Templates(directory="templates")


posts: list[dict] = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the content of the first post.",
        "author": "John Doe",
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "author": "Jane Smith",
    }
]



@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, 'title': "Home Page",})


@app.get("/api/posts")
def get_posts():
    return posts
