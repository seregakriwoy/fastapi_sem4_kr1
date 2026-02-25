from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    html_path = "index.html"
    return FileResponse(html_path)
