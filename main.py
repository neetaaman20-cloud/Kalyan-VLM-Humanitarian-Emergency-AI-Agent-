from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import httpx
import shutil
import os

app = FastAPI()

# 1. THE BRIDGE (CORS): This allows your React website to talk to Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any local website to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. THE AI BRAIN: This talks to Ollama (Moondream)
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    # Save the uploaded photo temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Create the prompt for humanitarian first aid
    prompt = "Analyze this image for humanitarian emergency safety. If there is an injury like a burn, provide immediate triage steps."

    try:
        # Call Ollama locally on your Mac
        async with httpx.AsyncClient() as client:
            # Note: We are sending the file name; you may need to convert 
            # the image to base64 if Ollama requires the raw data.
            response = await client.post(OLLAMA_URL, json={
                "model": "moondream",
                "prompt": prompt,
                "stream": False
            })
            result = response.json()
            analysis = result.get("response", "AI could not generate a response.")
    except Exception as e:
        analysis = f"Error connecting to Ollama: {str(e)}"
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return {"analysis": analysis}

@app.get("/")
def read_root():
    return {"status": "Kalyan-VLM Backend is Running"}