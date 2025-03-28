const axios = require("axios");

const FASTAPI_URL = process.env.RENALIA_API_URL || "http://localhost:8000/chat";

exports.askRenalIA = async (req, res) => {
  try {
    const { message, user_name } = req.body;

    const response = await axios.post(FASTAPI_URL, {
      message,
      user_name: user_name || ""
    });

    res.status(200).json(response.data);
  } catch (error) {
    console.error("❌ Erreur avec RenalIA :", error.message);
    res.status(500).json({ error: "Erreur lors de la communication avec RenalIA." });
  }
};
