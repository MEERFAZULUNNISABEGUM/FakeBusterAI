from fastapi import APIRouter
from services.trust_score import calculate_trust_score

router = APIRouter(tags=["Trust"])

@router.get("/trustscore")
def get_trust_score():
    return calculate_trust_score(phishing_risk=30, url_risk=25, deepfake_auth=85)
