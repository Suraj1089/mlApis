from re import TEMPLATE
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
# from src.model import spell_number
from pathlib import Path
import os

app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'app\\templates')

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = int(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
