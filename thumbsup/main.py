from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()


app.mount("/static", StaticFiles(directory="thumbsup/static"), name="static")

templates = Jinja2Templates(directory="thumbsup/templates")

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("thumbsup.html", {"request": request})

