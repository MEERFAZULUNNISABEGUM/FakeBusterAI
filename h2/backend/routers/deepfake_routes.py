from fastapi import APIRouter, UploadFile, File
from services.deepfake_detector import analyze_media

router = APIRouter(prefix="/detect", tags=["Deepfake"])

@router.post("/deepfake")
async def detect_deepfake(file: UploadFile = File(...)):
    contents = await file.read()
    return analyze_media(file.filename, contents)
