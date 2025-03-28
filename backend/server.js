const express = require('express')
const dotenv = require("dotenv")
const cors = require("cors")
const app = express()
const port = 5000
const sequelize = require('./config/database'); 

dotenv.config();

app.use(express.json());
app.use(cors())


/// connexion à la base de données


sequelize.authenticate()
  .then(() => {
    console.log('✅ Connexion à la base de données réussie.');
    return sequelize.sync(); // ← Synchronise tous les modèles
  })
  .then(() => {
    console.log('✅ Modèles synchronisés.');
  })
  .catch((err) => {
    console.error('❌ Erreur de connexion à la base :', err);
  });


const chatRoute = require('./routes/chatRoute');
const userRoute = require('./routes/userRoute');
const authRoute = require('./routes/authRoute');
const renalIARoute = require("./routes/renalIARoute");


app.use("/api/users", userRoute);
app.use("/api/auth", authRoute);

app.use('/api/chat', chatRoute);
app.use("/api/renal-ia", renalIARoute);

app.listen(port, () => {
    console.log(`RENTAI BACKEND  http://localhost:${port}`)
})