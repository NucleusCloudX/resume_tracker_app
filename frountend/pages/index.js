import React, { useState } from "react";
import axios from "axios";

const Index = () => {
  const [email, setEmail] = useState("");
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [matchScore, setMatchScore] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!email || !resume || !jobDescription) {
      alert("Please provide all details");
      return;
    }
    const formData = new FormData();
    formData.append("email", email);
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    setLoading(true);
    try {
      // Make sure your backend is running at this URL or update accordingly
      const response = await axios.post("http://localhost:5000/upload-resume", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      // After uploading the resume, you can call the matching endpoint.
      const matchResponse = await axios.post("http://localhost:5000/match", { email });
      setMatchScore(matchResponse.data.match_score);
    } catch (error) {
      console.error("Upload failed:", error);
      alert("Upload failed");
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "2rem" }}>
      <h1>Resume Matcher</h1>
      <input
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{ width: "100%", padding: "0.5rem", marginBottom: "1rem" }}
      />
      <input
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => setResume(e.target.files[0])}
        style={{ marginBottom: "1rem" }}
      />
      <textarea
        placeholder="Paste Job Description"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        rows={5}
        style={{ width: "100%", padding: "0.5rem", marginBottom: "1rem" }}
      />
      <button onClick={handleUpload} disabled={loading} style={{ padding: "0.75rem 1.5rem" }}>
        {loading ? "Uploading..." : "Upload & Match"}
      </button>
      {matchScore !== null && <p>Match Score: {matchScore}%</p>}
    </div>
  );
};

export default Index;
