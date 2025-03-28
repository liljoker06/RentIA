const express = require('express')
const dotenv = require("dotenv")
const cors = require("cors")
const app = express()
const port = 5000

dotenv.config();

app.use(express.json());
app.use(cors())


const chatRoute = require('./routes/chatRoute');
const userRoute = require('./routes/userRoute');
const authRoute = require('./routes/authRoute');
const renalIARoute = require("./routes/renalIARoute");


app.use("/api/users", userRoute);
app.use("/api/auth", authRoute);

app.use('/api/chat', chatRoute);
app.use("/api/renal-ia", renalIARoute);

app.listen(port, () => {
    console.log(`Example app listening on http://localhost:${port}`)
})