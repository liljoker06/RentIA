import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

export const askRenalIA = async (message, user_name) => {
  try {
    const response = await axios.post(`${API_URL}/api/renal-ia`, {
      message,
      user_name,
    });

    return response.data.response; 
  } catch (error) {
    console.error("Erreur RenalIA:", error);
    throw new Error("Une erreur est survenue avec l'IA");
  }
};
