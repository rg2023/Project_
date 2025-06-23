from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils.storage import upload_file, get_files
from app.utils.database import insert_data
# from app.utils.vertex import analyze_text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    bucket_name = "bucket_sandbox-lz-rachelge"
    try:
        upload_file(bucket_name, file.file, file.filename)
        return {"status": "success", "message": "File uploaded successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/upload")
def list_files():
    bucket_name = "bucket_sandbox-lz-rachelge"
    files = get_files(bucket_name)
    return {"files": files}



@app.post("/save")
async def save(data: dict):
    try:
        name = data["name"]
        value = data["value"]
        insert_data(name, value, "sandbox-lz-rachelge")
        return {"status": "success", "message": "Saved to DB"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# @app.post("/analyze")
# async def analyze(data: dict):
#     result = analyze_text(data['text'])
#     return {"result": result}

