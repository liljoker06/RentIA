require('dotenv').config();
const { Sequelize } = require('sequelize');
const fs = require('fs');
const path = require('path');

const sequelize = new Sequelize(
  process.env.DB_NAME,
  process.env.DB_USER,
  process.env.DB_PASSWORD,
  {
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    logging: false,
    dialect: 'mysql',
  }
);

// Chargement dynamique des modèles
const modelsDir = path.join(__dirname, '..', 'models');

fs.readdirSync(modelsDir).forEach((file) => {
  if (file.startsWith('model') && file.endsWith('.js')) {
    const defineModel = require(path.join(modelsDir, file));
    if (typeof defineModel === 'function') {
      defineModel(sequelize); 
    }
  }
});

module.exports = sequelize;
