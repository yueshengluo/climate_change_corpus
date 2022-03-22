from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers import query

router = APIRouter()
templates = Jinja2Templates(directory="templates/")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
#result = querydata('climate','science','concerned')
#print(result)

@router.get("/search", response_class=HTMLResponse)
def get_search(request: Request):
    tag = "politics"
    tag2 = "concerned"
    result = "Type a number"
    number = 'climate change'
    return templates.TemplateResponse('search.html', context={'request': request, 'number': number, 'result': result, 'tag': tag, 'tag2': tag2})


@router.post("/search", response_class=HTMLResponse)
def post_search(request: Request, tag: str = Form(...), tag2: str = Form(...),number: str = Form(...)):
    result = query.querydata(number,tag,tag2)
    #print(tag,tag2)
    return templates.TemplateResponse('search.html', context={'request': request, 'number': number, 'tag': tag,'tag2': tag2,'result': result,'yourword': number})