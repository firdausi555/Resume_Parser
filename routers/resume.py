# from fastapi import APIRouter, UploadFile, File, HTTPException
# from services.parser import extract_text_from_pdf, extract_info_from_text

# router = APIRouter(prefix="/resume", tags=["Resume"])

# @router.post("/upload")
# async def upload_resume(file: UploadFile = File(...)):
#     if file.content_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Only PDF files are allowed")

#     contents = await file.read()
#     text = extract_text_from_pdf(contents)
#     parsed_data = extract_info_from_text(text)
#     return {"parsed_data": parsed_data}


from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.parser import extract_text_from_pdf, extract_info_from_text

router = APIRouter(prefix="/resume", tags=["Resume"])

templates = Jinja2Templates(directory="templates")

@router.post("/upload", response_class=HTMLResponse)
async def upload_resume(request: Request, file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Only PDF files are allowed"
        })

    contents = await file.read()
    text = extract_text_from_pdf(contents)
    parsed_data = extract_info_from_text(text)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "parsed_data": parsed_data
    })
