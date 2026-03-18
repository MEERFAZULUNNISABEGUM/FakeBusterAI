from fastapi import APIRouter
from pydantic import BaseModel
from services.url_detector import analyze_url

router = APIRouter(prefix="/detect", tags=["URL"])

class URLRequest(BaseModel):
    url: str

@router.post("/url")
def detect_url(request: URLRequest):
    return analyze_url(request.url)
