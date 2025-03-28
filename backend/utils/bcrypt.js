const {hash, compare} = require("bcrypt");

const hashPassword = async (myPlaintextPassword, saltRounds = 10) => {
    return await hash(myPlaintextPassword, saltRounds);
}

const checkPassword = async (myPlaintextPassword, passwordHash) => {
    return await compare(myPlaintextPassword, passwordHash);
}

module.exports = {
    hashPassword,
    checkPassword
}