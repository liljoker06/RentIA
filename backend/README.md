# RentIa Backend

## Description

RentIa Backend est une API backend pour la gestion de locations immobilières. Ce projet utilise Express.js pour le
serveur, Sequelize pour interagir avec la base de données MySQL, et JWT pour l'authentification des utilisateurs.

## Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

- [Node.js](https://nodejs.org/) (version recommandée : `v16.x.x` ou plus)
- [MySQL](https://www.mysql.com/) (version recommandée : `8.x.x` ou plus)

## Installation

### 1. Installer les dépendances

Une fois dans le dossier du projet, installez les dépendances nécessaires via npm :

```bash
npm install
```

### 2. Configuration des variables d’environnement

Créez un fichier .env et ajoutez les variables suivantes :

```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=rent-ia
DB_USER=
DB_PASSWORD=
JWT_SECRET=Jwt
```

### 3. Démarrer la base de données

Assurez-vous que votre instance MySQL est en cours d’exécution et que la base de données rent-ia est créée.

Vous pouvez créer la base de données avec la commande suivante dans MySQL :


```
CREATE DATABASE rent-ia;
```

### 4. Démarrer le serveur
Pour démarrer le serveur en mode développement, utilisez la commande suivante :

```
npm run dev
```
Le serveur sera alors accessible sur http://localhost:3000.
