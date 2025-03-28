const User = require('../models/UserModel');
const {checkPassword} = require("../utils/bcrypt");
const {generateToken} = require("../utils/jwt");

const loginUser = async (req, res) => {
    const {email, password} = req.body;

    try {
        const user = await User.findOne({where: {email: email.toLowerCase()}})


        if (user && await checkPassword(password, user.password)) {
            const token = await generateToken(user.dataValues)
            res.status(200).json({token})
        } else {
            res.status(401).send({error: "Email ou mot de passe incorrect"});
        }
    } catch (e) {
        console.log(e)
        res.status(500).json({error: "Erreur lors de l'authentification"});
    }
};

module.exports = {
    loginUser
}