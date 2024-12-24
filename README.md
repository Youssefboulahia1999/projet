## 📝 **Description**
Cette API REST développée avec **Flask** permet de gérer une bibliothèque de livres. Les utilisateurs peuvent consulter, ajouter, modifier, supprimer et filtrer des livres via des appels API.

## 🚀 **Fonctionnalités**

- **GET /api/v1/resources/Livres/all** : Récupère la liste complète des livres.
- **GET /api/v1/resources/Livres?id=ID** : Récupère un livre par son identifiant.
- **POST /api/v1/resources/Livres** : Ajoute un nouveau livre.
- **PUT /api/v1/resources/Livres/<id>** : Met à jour les informations d'un livre existant.
- **DELETE /api/v1/resources/Livres/<id>** : Supprime un livre par son identifiant.
- **GET /api/v1/resources/Livres/filter** : Filtre les livres par nom ou ventes minimales.

## ⚙️ **Installation**

1. Clonez le projet :
   ```bash
   git clone <lien_du_repository>
   cd <nom_du_dossier>
   ```
2. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Installez les dépendances :
   ```bash
   pip install flask
   ```
4. Lancez l'application :
   ```bash
   python app.py
   ```
5. Accédez à l'API via :
   ```
   http://127.0.0.1:5000/
   ```
## 📊 **Exemples d'appels API**

- **Obtenir tous les livres :**
   ```bash
   curl -X GET "http://localhost:5000/api/v1/resources/Livres/all"
   ```
- **Ajouter un livre :**
   ```bash
   curl -X POST "http://localhost:5000/api/v1/resources/Livres" -H "Content-Type: application/json" -d '{"id": 3, "Nom": "Nouveau Livre", "Genre": "Roman", "Auteur": "Auteur Test", "Vente": 25}'
   ```
- **Mettre à jour un livre :**
   ```bash
   curl -X PUT "http://localhost:5000/api/v1/resources/Livres/3" -H "Content-Type: application/json" -d '{"Vente": 30}'
   ```
- **Supprimer un livre :**
   ```bash
   curl -X DELETE "http://localhost:5000/api/v1/resources/Livres/3"
   ```

---

## 🛠️ **Technologies Utilisées**
- **Python**
- **Flask**
