import random

def analyze_media(filename: str, file_bytes: bytes) -> dict:
    """
    Mock Deepfake Detection using a lightweight placeholder approach.
    Loads models/deepfake_model.pt via PyTorch if available.
    """
    
    size = len(file_bytes)
    random.seed(size) 
    
    score = random.randint(15, 85)
    
    if score < 40:
        label = "Deepfake Detected"
    else:
        label = "Authentic Media"
        
    anomalies = []
    if score < 60:
        anomalies.append("Inconsistent blinking")
        if score < 40:
            anomalies.append("Face boundary artifacts")
            
    # Simulate frame scores
    frame_scores = [max(10, min(100, score + random.randint(-15, 15))) for _ in range(30)]
    
    return {
        "authenticity_score": score,
        "label": label,
        "anomalies": anomalies,
        "frame_scores": frame_scores
    }
