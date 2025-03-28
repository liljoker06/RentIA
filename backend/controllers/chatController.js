// controllers/chatController.js
const axios = require('axios');

const FASTAPI_URL = process.env.FASTAPI_URL || 'http://localhost:8000';

exports.sendMessageToAI = async (req, res) => {
  try {
    const { message } = req.body;

    const response = await axios.post(`${FASTAPI_URL}/chat`, { message });

    res.status(200).json(response.data);
  } catch (error) {
    console.error('Erreur lors de l\'appel à FastAPI :', error.message);
    res.status(500).json({ error: 'Erreur côté IA' });
  }
};
