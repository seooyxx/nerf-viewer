from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# 정적 파일 경로 설정을 현재 디렉터리로 수정
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def read_index():
    # 현재 디렉터리 내의 index.html로 경로 수정
    return FileResponse('index.html')