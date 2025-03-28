const express = require('express')
const dotenv = require("dotenv")
const cors = require("cors")
const app = express()
const port = 3000

dotenv.config();

app.use(express.json());
app.use(cors())

app.use("/api/users", require("./routes/userRoute"));
app.use("/api/auth", require("./routes/authRoute"));

app.listen(port, () => {
    console.log(`Example app listening on http://localhost:${port}`)
})