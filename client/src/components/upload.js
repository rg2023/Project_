import { useState } from "react";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);
    const API_URL = window.VITE_BACKEND_URL;
    const res = await fetch(`${API_URL}/upload`, {
      method: "POST",
      body: formData,
    });

    const result = await res.json();
    setMessage(result.message);
  };

  return (
    <div className="space-y-4">
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="block"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Upload
      </button>
      <p>{message}</p>
    </div>
  );
}
