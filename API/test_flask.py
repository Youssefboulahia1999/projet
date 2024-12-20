# import flask
# from flask import request, jsonify

# # Création de l'objet Flask
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Annuaire Internet</h1>
#               <p>Ce site est le prototype d’une API mettant à disposition des données sur les livres d’une entreprise.</p>'''

# Livres = [
# {'id': 0, 'Nom': 'Dupont', 'Genre': 'Jean', 'Auteur': 'Développeur', 'Vente': 5},
# {'id': 1, 'Nom': 'Durand', 'Genre': 'Elodie', 'Auteur': 'Directrice Commerciale', 'Vente':
# 4},
# {'id': 2, 'Nom': 'Lucas', 'Genre': 'Jérémie', 'Auteur': 'DRH', 'Vente': 4}
# ]
# @app.route('/api/v1/resources/Livres/all', methods=['GET'])
# def api_all():
#     return jsonify(Livres)

# @app.route('/api/v1/resources/Livres',methods=['GET'])
# def api_id():
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Erreur : Pas d’identifiant fourni.Veuillez spécifier un id."
#     results = [Livre for Livre in Livres if Livre['id'] == id]
# return jsonify(results)


# @app.route('/api/v1/resources/Livres', methods=['GET'])
# def api_id():
#     # Vérification si l'identifiant est présent dans les arguments
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Erreur : Pas d’identifiant fourni. Veuillez spécifier un id.", 400

#     # Filtrage des résultats
#     results = [Livre for Livre in Livres if Livre['id'] == id]

#     # Renvoi des résultats sous forme JSON
#     return jsonify(results)

# # Démarrage de l'application
# if __name__ == '__main__':
#     app.run()
# 




import flask
from flask import request, jsonify

# Création de l'objet Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Liste des Livres
Livres = [
    {'id': 0, 'Nom': '1001 nuit', 'Genre': 'Conte merveilleux', 'Auteur': 'Inconnu', 'Vente': 30},
    {'id': 1, 'Nom': 'hercules poirot', 'Genre': 'Roman', 'Auteur': 'Agatha Christie', 'Vente': 16},
    {'id': 2, 'Nom': 'Moby-Dick', 'Genre': 'roman', 'Auteur': 'Herman Melville', 'Vente': 11}
]

# Page d'accueil
@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>Annuaire Internet</h1>
    <p>Ce site est le prototype d’une API mettant à disposition des données sur les livres. <br>
    curl -X GET "http://localhost:5000/api/v1/resources/Livres?id=2" <br>
    curl -X GET "http://localhost:5000/api/v1/resources/Livres/all"<br>
    curl -X POST "http://localhost:5000/api/v1/resources/Livres" \<br>
-H "Content-Type: application/json" \<br>
-d '{<br>
    "id": 3,<br>
    "Nom": "dialogue",<br>
    "Genre": "l'Encyclopédie",<br>
    "Auteur": "diderot",<br>
    "Vente": 20<br>
}'<br>
curl -X PUT "http://localhost:5000/api/v1/resources/Livres/3" \<br>
-H "Content-Type: application/json" \<br>
-d '{<br>
    "Auteur": "diderot",<br>
    "Vente": 30<br>
}'<br>
curl -X DELETE "http://localhost:5000/api/v1/resources/Livres/3"<br>
<br>


    http://127.0.0.1:5000/api/v1/resources/Livres/all : pour un (GET) complet <br>
    http://127.0.0.1:5000/api/v1/resources/Livres?id=2 pour id 2 ex <br>
    http://127.0.0.1:5000/api/v1/resources/Livres/filter : pour filtrage des resultas <br>
    http://127.0.0.1:5000/api/v1/resources/Livres/3 : methode (DELETE) <br>


    http://127.0.0.1:5000/api/v1/resources/Livres/3 : (PUT) <br>
    { <br>
    "Auteur": "Lead Designer", <br>
    "Vente": 3 <br>
    } <br>



    http://127.0.0.1:5000/api/v1/resources/Livres : (POST)<br>
    { <br>
    "id": 3, <br>
    "Nom": "Martin", <br>
    "Genre": "Paul", <br>
    "Auteur": "Designer", <br>
    "Vente": 2 <br>
    } <br>
</p>
    '''

# Obtenir tous les livres
@app.route('/api/v1/resources/Livres/all', methods=['GET'])
def api_all():
    return jsonify(Livres)

# Obtenir un livre par son ID
@app.route('/api/v1/resources/Livres', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Erreur : Pas d’identifiant fourni. Veuillez spécifier un id.", 400

    results = [Livre for Livre in Livres if Livre['id'] == id]
    return jsonify(results)

# Ajouter un nouvel livre (POST)
@app.route('/api/v1/resources/Livres', methods=['POST'])
def add_Livre():
    new_Livre = request.get_json()

    # Vérification des champs requis
    if not all(key in new_Livre for key in ['id', 'Nom', 'Genre', 'Auteur', 'Vente']):
        return "Erreur : Les champs 'id', 'Nom', 'Genre', 'Auteur', et 'Vente' sont requis.", 400

    # Vérifier si l'ID existe déjà
    if any(emp['id'] == new_Livre['id'] for emp in Livres):
        return "Erreur : Un livre avec cet ID existe déjà.", 400

    # Ajouter l'livre
    Livres.append(new_Livre)
    return jsonify({"message": "livre ajouté avec succès.", "livre": new_Livre}), 201

# Mettre à jour un livre existant (PUT)
@app.route('/api/v1/resources/Livres/<int:id>', methods=['PUT'])
def update_Livre(id):
    updated_data = request.get_json()
    for Livre in Livres:
        if Livre['id'] == id:
            Livre.update(updated_data)
            return jsonify({"message": "livre mis à jour avec succès.", "livre": Livre}), 200

    return "Erreur : Aucun livre trouvé avec cet ID.", 404

# Supprimer un livre (DELETE)
@app.route('/api/v1/resources/Livres/<int:id>', methods=['DELETE'])
def delete_Livre(id):
    global Livres
    Livres = [emp for emp in Livres if emp['id'] != id]
    return jsonify({"message": f"livre avec l'ID {id} supprimé avec succès."}), 200

# Gestion des erreurs 404
@app.errorhandler(404)
def page_not_found(e):
    return flask.jsonify({"error": "Page not found"}), 404

# Filtrer les livres
@app.route('/api/v1/resources/Livres/filter', methods=['GET'])
def filter_Livres():
    nom = request.args.get('nom')
    vente_min = request.args.get('vente_min')

    if not nom and not vente_min:
        return "Erreur : Aucun filtre fourni. Veuillez spécifier 'nom' ou 'vente_min'.", 400

    filtered_Livres = Livres
    if nom:
        filtered_Livres = [emp for emp in filtered_Livres if emp['Nom'].lower() == nom.lower()]
    if vente_min:
        try:
            vente_min = int(vente_min)
            filtered_Livres = [emp for emp in filtered_Livres if emp['Vente'] >= vente_min]
        except ValueError:
            return "Erreur : 'vente_min' doit être un entier.", 400

    if not filtered_Livres:
        return "Aucun livre ne correspond aux critères spécifiés.", 404

    return jsonify(filtered_Livres)

# Démarrage de l'application
if __name__ == '__main__':
    app.run()


