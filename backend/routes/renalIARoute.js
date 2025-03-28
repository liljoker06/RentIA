const express = require("express");
const router = express.Router();
const { askRenalIA } = require("../controllers/renalIAController");

router.post("/", askRenalIA);

module.exports = router;
