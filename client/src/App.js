import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import Home from "./components/home";
import Upload from "./components/upload";
import FilesList from "./components/fileslist";
import SaveForm from "./components/save";

export default function App() {
  return (
    <Router>
      <div className="p-4">
        <nav className="mb-4 space-x-4">
          <Link to="/" className="text-blue-500 hover:underline">Home</Link>
          <Link to="/upload" className="text-blue-500 hover:underline">Upload</Link>
          <Link to="/files" className="text-blue-500 hover:underline">Files</Link>
          <Link to="/save" className="text-blue-500 hover:underline">Save Data</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/upload" element={<Upload />} />
          <Route path="/files" element={<FilesList />} />
          <Route path="/save" element={<SaveForm />} />
        </Routes>
      </div>
    </Router>
  );
}
