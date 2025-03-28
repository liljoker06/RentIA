// routes/chatRoute.js
const express = require('express');
const router = express.Router();
const { sendMessageToAI } = require('../controllers/chatController');

router.post('/', sendMessageToAI);

module.exports = router;
