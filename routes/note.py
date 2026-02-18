from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from config.db import conn
from fastapi.templating import Jinja2Templates


note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    newDoc = []
    docs = conn.notes.notes.find({})
    for doc in docs:
        newDoc.append(
            {
                "id": doc["_id"],
                "title": doc["title"],
                "desc": doc["desc"],
                "important": doc["important"],
            }
        )
    return templates.TemplateResponse(
        request=request, name="index.html", context={"newDoc": newDoc}
    )


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    print(f"note from POST form----{form}")
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    # note = conn.notes.notes.insert_one(formDict)
    # return {"Success": True}
    return templates.TemplateResponse(
        "index.html", {"request": request, "success": "Form submitted successfully!"}
    )


# @note.delete("/")
# def delete_item(requ)
