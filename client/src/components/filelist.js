import { useEffect, useState } from "react";

export default function FilesList() {
  const [files, setFiles] = useState([]);
  const API_URL = window.VITE_BACKEND_URL;
  useEffect(() => {
    fetch(`${API_URL}/upload`)
      .then((res) => res.json())
      .then((data) => setFiles(data.files || []));
  }, []);

  return (
    <div>
      <h2 className="text-lg font-semibold mb-2">Uploaded Files:</h2>
      <ul className="list-disc pl-6">
        {files.map((file, i) => (
          <li key={i}>{file}</li>
        ))}
      </ul>
    </div>
  );
}
