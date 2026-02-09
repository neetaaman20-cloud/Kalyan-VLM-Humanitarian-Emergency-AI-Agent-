# 🌍 Kalyan-VLM: Humanitarian Emergency AI Agent

**Kalyan-VLM** is a local-first, privacy-focused AI vision tool built to provide instant humanitarian safety analysis and triage steps in emergency situations. It uses a Multimodal Vision-Language Model (VLM) to analyze images directly on your hardware.

### 🚀 Key Features
* **Privacy-First Vision:** Analyzes humanitarian/medical images locally on your Mac using **Ollama** and **Moondream**—no sensitive data ever leaves your computer.
* **Instant Safety Analysis:** Provides immediate triage steps and hazard identification for first responders or individuals.
* **Full-Stack Architecture:** Combines a responsive **React** frontend with a high-performance **FastAPI** backend.
* **Zero API Costs:** Runs entirely on local compute, making it accessible for humanitarian work in remote areas.

### 🛠️ Tech Stack
* **Frontend:** React.js
* **Backend:** FastAPI (Python)
* **AI Engine:** Ollama with the **Moondream** model
* **Environment:** Optimized for Apple Silicon (MacBook Air)

---

## 💻 How to Run and Test

Follow these steps to get the agent running on your local machine:

### 1. Prerequisites
Ensure you have the following installed:
* **Node.js** (for the frontend)
* **Python 3.9+** (for the backend)
* **Ollama** (to run the AI model locally)

### 2. Prepare the AI Model
Open your terminal and pull the vision model:
```bash
ollama pull moondream
3. Setup the Backend (Terminal 1)

Navigate to the project folder and install Python dependencies:

Bash
pip install fastapi uvicorn httpx
python3 -m uvicorn main:app --reload
4. Setup the Frontend (Terminal 2)

In a new terminal window, install React dependencies and start the UI:

Bash
npm install
npm start
5. Testing

Open your browser to http://localhost:3000.

Upload an image of a hazard (e.g., a burn or a first-aid scenario).

Click Analyze Safety to receive an AI-generated humanitarian action plan.
