from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/viewer.html")
async def read_viewer():
    return FileResponse('viewer.html')

@app.get("/test.html")
async def read_viewer():
    return FileResponse('test.html')


@app.get("/data/{file_path:path}")
async def read_data_file(file_path: str):
    file_location = os.path.join("data", file_path)
    if os.path.isfile(file_location):
        return FileResponse(file_location)
    else:
        raise HTTPException(status_code=404, detail="File not found")
