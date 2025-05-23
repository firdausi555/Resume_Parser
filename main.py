# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from fastapi.middleware.cors import CORSMiddleware
# from routers import resume

# app = FastAPI(title="Resume Parser API")

# # Enable CORS to allow frontend JS to talk to backend
# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/", response_class=HTMLResponse)
# async def root():
#     with open("index.html", "r") as f:
#         return f.read()

# app.include_router(resume.router)

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routers import resume

app = FastAPI(title="Resume Parser API")
app.include_router(resume.router)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
