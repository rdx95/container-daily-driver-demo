from fastapi import FastAPI, File, UploadFile, HTTPException
from app.storage import upload_file_to_s3
from app.models import FileMeta
import os
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

MONGO_URL = os.environ["MONGO_URL"]
client = AsyncIOMotorClient(MONGO_URL)
db = client["file_db"]
files_collection = db["files"]

@app.get("/")
def read_root():
    return {"message": "FastAPI with MongoDB and MinIO"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        s3_url = await upload_file_to_s3(file)
        metadata = FileMeta(filename=file.filename, url=s3_url)
        await files_collection.insert_one(metadata.dict())
        return {"status": "uploaded", "url": s3_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
