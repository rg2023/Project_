import { useState } from "react";

export default function SaveForm() {
  const [name, setName] = useState("");
  const [value, setValue] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async () => {
    const API_URL = window.VITE_BACKEND_URL;
    const res = await fetch(`${API_URL}/save`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, value }),
    });

    const result = await res.json();
    setMessage(result.message);
  };

  return (
    <div className="space-y-4">
      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="border p-2 w-full"
      />
      <input
        placeholder="Value"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className="border p-2 w-full"
      />
      <button
        onClick={handleSubmit}
        className="bg-green-600 text-white px-4 py-2 rounded"
      >
        Save
      </button>
      <p>{message}</p>
    </div>
  );
}
