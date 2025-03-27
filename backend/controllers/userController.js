const User = require('../models/userModel');
const {hashPassword} = require("../utils/bcrypt");

// Créer un utilisateur
const createUser = async (req, res) => {
    try {
        const {name, email, password} = req.body;
        const newUser = await User.create({name, email, password: await hashPassword(password)});
        return res.status(201).json(newUser);
    } catch (error) {
        console.error(error);
        return res.status(500).json({message: 'Erreur lors de la création de l\'utilisateur'});
    }
};

// Récupérer un utilisateur par son ID
const getUserById = async (req, res) => {
    try {
        const userId = req.params.id;
        const user = await User.findByPk(userId);
        if (!user) {
            return res.status(404).json({message: 'Utilisateur non trouvé'});
        }
        return res.status(200).json(user);
    } catch (error) {
        console.error(error);
        return res.status(500).json({message: 'Erreur lors de la récupération de l\'utilisateur'});
    }
};

// Mettre à jour un utilisateur
const updateUser = async (req, res) => {
    try {
        const userId = req.params.id;
        const {name, email, password} = req.body;
        const user = await User.findByPk(userId);

        if (!user) {
            return res.status(404).json({message: 'Utilisateur non trouvé'});
        }

        user.name = name || user.name;
        user.email = email || user.email;
        user.password = password || user.password;

        await user.save();
        return res.status(200).json({message: 'Utilisateur mis à jour avec succès', user});
    } catch (error) {
        console.error(error);
        return res.status(500).json({message: 'Erreur lors de la mise à jour de l\'utilisateur'});
    }
};

// Supprimer un utilisateur
const deleteUser = async (req, res) => {
    try {
        const userId = req.params.id;
        const user = await User.findByPk(userId);

        if (!user) {
            return res.status(404).json({message: 'Utilisateur non trouvé'});
        }

        await user.destroy();
        return res.status(200).json({message: 'Utilisateur supprimé avec succès'});
    } catch (error) {
        console.error(error);
        return res.status(500).json({message: 'Erreur lors de la suppression de l\'utilisateur'});
    }
};

module.exports = {
    createUser,
    updateUser,
    getUserById,
    deleteUser
}