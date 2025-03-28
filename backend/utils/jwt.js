const jwt = require("jsonwebtoken");

const generateToken = (data) => {
    return jwt.sign(data, process.env.JWT_SECRET, {expiresIn: "30d"});
}

const verifyToken = (token) => {
    return jwt.verify(token, process.env.JWT_SECRET);
}

module.exports = {
    generateToken,
    verifyToken
}
