from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# static 폴더 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates 폴더 연결
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request): # HTML return
    return templates. TemplateResponse(request=request, name="main.html")