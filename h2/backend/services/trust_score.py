def calculate_trust_score(phishing_risk: int = 50, url_risk: int = 50, deepfake_auth: int = 50) -> dict:
    ts = ((100 - phishing_risk) * 0.4) + ((100 - url_risk) * 0.3) + (deepfake_auth * 0.3)
    return {
        "overall_trust_score": round(ts, 1)
    }
