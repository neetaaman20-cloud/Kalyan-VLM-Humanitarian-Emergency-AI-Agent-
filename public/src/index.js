import React from 'react';
import ReactDOM from 'react-dom/client';
import App from '/App'; // This now points to the file we renamed to 'App.js'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);