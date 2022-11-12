from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os

# servce static files
from fastapi.staticfiles import StaticFiles


app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'app\\templates')

templates = Jinja2Templates(directory=TEMPLATES_DIR)

# serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})
