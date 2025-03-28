# RentIA

## 📄 Présentation du projet

RentIA est une application web alimentée par l'intelligence artificielle, conçue pour aider les utilisateurs à trouver des logements correspondant à leurs besoins.

## 📚 Stack technologique

- **Frontend** : React
- **Backend** : Node.js, Express.js, Sequelize, MySQL
- **Style** : Tailwind CSS
- **Outil de build** : Vite
- **Authentification** : JWT
- **IA** : Python, FastAPI, PyTorch

---

## 🗂️ Structure du projet

```
RentIA/
│
├── backend/          # Services backend
│   ├── src/
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
│   ├── src/
│   │   ├── api/      # Fichiers liés à l’API
│   │   ├── assets/   # Ressources du projet (images, icônes, etc.)
│   │   ├── components/ # Composants React réutilisables
│   │   └── pages/    # Pages de l’application
│   ├── index.html    # Point d’entrée HTML
│   ├── package.json  # Dépendances et configurations du frontend
│   └── tailwind.config.js  # Configuration Tailwind CSS
│
└── ia/               # Dossier pour les fichiers liés à l’intelligence artificielle
    ├── ai/              # Coeur de l'IA conversationnelle et de recommandation de logement
    │   ├── embeddings/  # Génération d’embeddings et modules de similarité
    │   ├── responder.py # Gère les réponses générées pour l'utilisateur
    │   └── retriever.py # Recherche de réponses pertinentes
    ├── controllers/     # Contrôleurs FastAPI pour les routes d'IA
    ├── models/          # Définition, entraînement et inférence du modèle
    ├── routes/          # Routes de l’API FastAPI
    ├── services/        # Services utilisés par l’IA
    ├── utils/           # Fonctions utilitaires
    ├── data/            # Données d'entraînement (datasets)
    ├── main.py          # Point d’entrée du serveur FastAPI
    └── requirements.txt  # Dépendances Python
```

---

## ✨ Fonctionnalités principales

- Authentification des utilisateurs (Frontend et Backend avec JWT)
- Gestion des propriétés locatives
- Interface utilisateur responsive
- Recommandation intelligente de logements via embeddings IA
- Prévision future : Chatbot entraînable et conversationnel en Python/FastAPI

---

## ⚡ Prérequis

### Frontend

- **Node.js** (version recommandée : v16.x.x ou plus)
- **npm** ou **yarn** (gestionnaire de paquets)

### Backend

- **Node.js** (version recommandée : v16.x.x ou plus)
- **MySQL** (version recommandée : 8.x.x ou plus)

### IA (FastAPI / Python)

- **Python** (version recommandée : 3.10 ou plus)
- **pip** (gestionnaire de paquets Python)

---

## 🚀 Installation

### 1. Cloner le dépôt
```bash
git clone <url-du-repository>
```

### 2. Backend
```bash
cd backend
npm install
```

Configurer le fichier `.env` :
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=rent-ia
DB_USER=<votre-utilisateur>
DB_PASSWORD=<votre-mot-de-passe>
JWT_SECRET=<votre-secret-jwt>
```

Démarrer le serveur :
```bash
npm run dev
```
Le backend sera accessible sur `http://localhost:5000`

### 3. Frontend
```bash
cd front
npm install
npm run dev
```
Le frontend sera accessible sur `http://localhost:5173`

### 4. IA (FastAPI)
```bash
cd ia
python -m venv venv
venv\Scripts\activate  # sous Windows
source venv/bin/activate  # sous Mac/Linux

pip install -r requirements.txt
```

Lancer le serveur FastAPI :
```bash
python main.py
```
Le serveur IA sera disponible sur `http://localhost:8000`

---

## 📊 Objectifs futurs

- Ajout d’une IA conversationnelle entraînée sur des dialogues utilisateurs
- Intégration de l’IA directement dans le frontend via des appels API
- Recommandation personnalisée en fonction du profil utilisateur

---

## 📍 Auteur

- Projet créé dans le cadre d’un projet éducatif

