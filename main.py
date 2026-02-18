import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient('mongodb+srv://shubhankarsaxena10:g3OFWoqgMmLdHDLb@cluster0.ndky7.mongodb.net')

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     newDoc = []
#     docs = conn.notes.notes.find({})
#     for doc in docs:
#         newDoc.append({
#             "id": doc['_id'],
#             "note": doc['note']
#         })
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={"newDoc": newDoc}
#     )


# @app.post("/", response_class=HTMLResponse)
# async def create_item(request: Request):
