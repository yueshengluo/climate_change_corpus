from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/accordion", response_class=HTMLResponse)
def get_accordion(request: Request):
    tag = "politics"
    tag2 = "concerned"
    result = "Type a number"
    return templates.TemplateResponse('accordion.html', context={'request': request, 'result': result, 'tag': tag, 'tag2': tag2, "first":1})


@router.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...),tag2: str = Form(...)):

    return templates.TemplateResponse('accordion.html', context={'request': request, 'tag': tag,'tag2': tag2, "first":0})
