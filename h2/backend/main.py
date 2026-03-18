import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers (we will create these next)
from routers import email_routes, url_routes, deepfake_routes, trust_routes

app = FastAPI(title="TrustShield AI Backend", version="1.0")

# Enable CORS for the Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
from routers import auth_routes
app.include_router(auth_routes.router)
app.include_router(email_routes.router)
app.include_router(url_routes.router)
app.include_router(deepfake_routes.router)
app.include_router(trust_routes.router)

@app.get("/")
def read_root():
    return {"message": "TrustShield AI API is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
