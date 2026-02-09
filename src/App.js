import React, { useState } from 'react';

function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState("");

  const handleUpload = async () => {
    if (!image) return alert("Please select an image first!");
    const formData = new FormData();
    formData.append('file', image);

    try {
      setResult("AI is analyzing for humanitarian safety...");
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResult(data.analysis);
    } catch (error) {
      setResult("Error: Backend unreachable. Check Terminal 1!");
    }
  };

  return (
    <div style={{ padding: '40px', textAlign: 'center', fontFamily: 'sans-serif' }}>
      <h1>🌍 Kalyan-VLM Emergency Agent</h1>
      <input type="file" onChange={(e) => setImage(e.target.files[0])} />
      <button onClick={handleUpload} style={{ marginLeft: '10px' }}>Analyze</button>
      <div style={{ marginTop: '20px', whiteSpace: 'pre-wrap', border: '1px solid #ddd', padding: '10px' }}>
        {result || "Waiting for upload..."}
      </div>
    </div>
  );
}

// THIS IS THE LINE index.js IS LOOKING FOR:
export default App;