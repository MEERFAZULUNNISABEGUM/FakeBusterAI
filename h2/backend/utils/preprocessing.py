import re

def clean_text(text: str) -> str:
    """Basic text cleaning."""
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()
