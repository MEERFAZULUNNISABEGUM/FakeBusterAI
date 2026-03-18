# TrustShield AI (FakeBuster AI)

TrustShield AI is an advanced "Threat Defense Platform" that provides comprehensive security scanning and analysis tools. 
It combines a modern, glassmorphism-styled Streamlit frontend with a robust FastAPI backend to detect phishing, malicious URLs, and deepfakes.

## Directory Structure
- `backend/`: FastAPI application containing all the API routes, ML models, and logic for threat detection.
- `frontend/`: Streamlit dashboard offering an interactive UI for the security tools.

## Key Features
- **System Dashboard**: Real-time threat detection and mitigation overview with a global defense matrix.
- **Email Analysis**: Neural email inspection and deep semantic analysis of email content to detect phishing and social engineering.
- **URL Scanner**: Quantum link analysis for real-time inspection of domains, redirects, and SSL signatures for malicious intent.
- **Deepfake Detection**: Advanced visual authenticity engine utilizing biometric and artifact analysis to detect AI-generated manipulation across images and videos.
- **Trust Score Analysis**: Global trust profiling and organization trust index.
- **System Analytics**: Deep dive into historical data, system performance, and threat landscapes with rich visualizations.
- **Authentication**: Custom modern login and signup interface.

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js (if applicable for certain UI tools or packaging)

### Running the Backend
Navigate to the `backend` directory and run the FastAPI server:
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Alternatively, you can run it via `uvicorn`:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at `http://localhost:8000`.

### Running the Frontend
Navigate to the `frontend` directory and run the Streamlit app:
```bash
cd frontend
pip install streamlit requests pandas plotly
streamlit run app.py
```
The web interface will be accessible at `http://localhost:8501` (by default).

## Technologies Used
- **Backend Framework:** FastAPI
- **Frontend Framework:** Streamlit
- **Data Visualization:** Plotly
- **Data Processing:** Pandas
