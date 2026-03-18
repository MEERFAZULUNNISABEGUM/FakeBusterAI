from fastapi import APIRouter
from pydantic import BaseModel
from services.email_detector import analyze_email

router = APIRouter(prefix="/detect", tags=["Email"])

class EmailRequest(BaseModel):
    content: str

@router.post("/email")
def detect_email(request: EmailRequest):
    return analyze_email(request.content)
