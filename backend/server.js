const express = require('express')
const dotenv = require("dotenv")
const cors = require("cors")
const app = express()
const port = 3000

dotenv.config();

app.use(express.json());
app.use(cors())


const chatRoute = require('./routes/chatRoute');
const userRoute = require('./routes/userRoute');
const authRoute = require('./routes/authRoute');

app.use("/api/users", userRoute);
app.use("/api/auth", authRoute);

app.use('/api/chat', chatRoute);


app.listen(port, () => {
    console.log(`Example app listening on http://localhost:${port}`)
})