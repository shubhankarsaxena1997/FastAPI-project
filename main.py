from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# load .env file to environment
load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient(os.getenv("connectionString"))

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
