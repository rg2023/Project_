from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils.storage import upload_file, get_files
# from app.utils.database import insert_data
# from app.utils.vertex import analyze_text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    bucket_name = "bucket-sandbox-lz-rachelge"
    upload_file_from_path(bucket_name, file.file)
    return {"message": "File uploaded"}


@app.get("/upload")
def list_files():
    bucket_name = "bucket-sandbox-lz-rachelge"
    files = get_files(bucket_name)
    return {"files": files}

# @app.post("/save")
# async def save(data: dict):
#     insert_data(data['name'], data['value'])
#     return {"message": "Saved to DB"}

# @app.post("/analyze")
# async def analyze(data: dict):
#     result = analyze_text(data['text'])
#     return {"result": result}

