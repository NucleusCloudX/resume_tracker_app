import axios from "axios";

const API_BASE_URL = "http://localhost:5000"; // Update this with your backend URL

export const uploadResume = async (formData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error uploading resume", error);
    throw error;
  }
};

export const getMatchScore = async (email) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/match-score?email=${email}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching match score", error);
    throw error;
  }
};
