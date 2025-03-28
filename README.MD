# RentIA

## Présentation du projet

RentIA est une application web alimentée par l'intelligence artificielle, conçue pour aider les utilisateurs à trouver des logements correspondant à leurs besoins.

## Stack technologique

- **Frontend** : React
- **Backend** : Node.js, Express.js, Sequelize, MySQL
- **Style** : Tailwind CSS
- **Outil de build** : Vite
- **Authentification** : JWT

---

## Structure du projet

```
RentIA/
│
├── backend/          # Services backend
│   ├── src/          # Code source du backend
│   │   ├── controllers/  # Contrôleurs pour gérer les requêtes API
│   │   ├── models/       # Modèles Sequelize pour la base de données
│   │   ├── routes/       # Routes de l’API
│   │   ├── services/     # Logique métier (authentification, gestion des propriétés)
│   │   └── app.js        # Point d’entrée du backend
│   ├── .env            # Variables d’environnement
│   ├── package.json    # Dépendances du backend
│   └── README.md       # Documentation du backend
│
├── front/            # Application frontend
│   ├── src/          # Code source de l’application
│   │   ├── api/      # Fichiers liés à l’API
│   │   ├── assets/   # Ressources du projet (images, icônes, etc.)
│   │   ├── components/ # Composants React réutilisables
│   │   ├── config/   # Fichiers de configuration
│   │   └── pages/    # Pages de l’application
│   │       ├── Home.jsx
│   │       ├── Login.jsx
│   │       ├── Register.jsx
│   │       └── App.jsx
│   ├── index.html    # Point d’entrée HTML
│   ├── package.json  # Dépendances et configurations du frontend
│   └── tailwind.config.js  # Configuration Tailwind CSS
│
└── ia/               # Dossier pour les fichiers liés à l’intelligence artificielle (à venir)
```

---

## Fonctionnalités principales

- Authentification des utilisateurs (Frontend et Backend avec JWT)
- Gestion des propriétés locatives
- Interface utilisateur responsive
- Design personnalisé avec Tailwind CSS

---

## Prérequis

### Frontend

- **Node.js** (version recommandée : `v16.x.x` ou plus)
- **npm** ou **yarn** (gestionnaire de paquets)

### Backend

- **Node.js** (version recommandée : `v16.x.x` ou plus)
- **MySQL** (version recommandée : `8.x.x` ou plus)

---

## Installation

1. Clonez le dépôt du frontend :
   ```bash
   git clone <url-du-repository>
   ```
   
2. Allez dans le dossier backend et installez les dépendances :
   ```bash
   npm install
   ```

3. Configurez les variables d’environnement dans le fichier .env :
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=rent-ia
   DB_USER=<votre-utilisateur>
   DB_PASSWORD=<votre-mot-de-passe>
   JWT_SECRET=<votre-secret-jwt>
   ```
   
4. Démarrez le serveur en mode développement :
   ```bash
   npm run dev
   ```
   Le serveur backend sera accessible sur http://localhost:3000.

### Démarrage de la base de données
Assurez-vous que votre instance MySQL est en cours d’exécution et que la base de données rent-ia est créée. Pour créer la base de données, exécutez la commande suivante dans MySQL :
   ```
   CREATE DATABASE rent-ia;
   ```