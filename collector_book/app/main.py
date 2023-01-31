from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .models import mongodb
from .models.book import BookModel

# server start > reload 는 release 에서 사용 X
# uvicorn app.main:app --reload
# python server.py
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword="python", publisher="public", price=1200, image="me.png")
    await mongodb.engine.save(book)  # DB 저장
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이"}
    )


# 서버가 켜질때 이벤트
@app.on_event("startup")
async def on_app_start():
    """before app starts"""
    mongodb.connect()


# 서버가 꺼질때 이벤트
@app.on_event("shutdown")
async def on_app_shutdown():
    """after app starts"""
    mongodb.close()
