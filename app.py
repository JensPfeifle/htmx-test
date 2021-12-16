# pylint: disable=missing-docstring

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

app = FastAPI()

# TODO:
# CSRF?, CORS
# 404/500 page

todos = [{"id": 1, "name": "Clean room"}]

templates = Jinja2Templates(directory="templates")


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")


@app.route("/")
def index(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})


@app.get("/todos")
def get_todos(request: Request):
    return templates.TemplateResponse(
        "bp/todos/todos.html", {"request": request, "todos": todos}
    )


@app.post("/todos/add")
def add_todo(request: Request, todo: str = Form(...)):
    num = len(todos) + 1
    todos.append({"id": num, "name": todo})
    return templates.TemplateResponse(
        "bp/todos/todos.html", {"request": request, "todos": todos}
    )
