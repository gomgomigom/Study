from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/items/{id}/{data}", response_class=HTMLResponse)
async def read_item(request: Request, id: str, data: str):

    return templates.TemplateResponse(
        "./item.html", {"request": request, "id": id, "data": data}
    )
