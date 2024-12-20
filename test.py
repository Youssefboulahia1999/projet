Tsanta Randriatsitohain11:10
REQUETE POST :

curl -X POST https://jsonplaceholder.typicode.com/comments -H "Content-Type: application/json" -d "{\"postId\": 1, \"name\": \"Nouveau commentaire\", \"email\": \"nouveau@commentaire.com\", \"body\": \"Ceci est un nouveau commentaire.\"}"

REQUETE PUT :

curl -X PUT https://jsonplaceholder.typicode.com/comments -H "Content-Type: application/json" -d "{\"postId\": 1000, \"name\": \"Nouveau commentaire\", \"email\": \"nouveau@commentaire.com\", \"body\": \"Ceci est un commentaire mis à jour.\"}"

Tsanta Randriatsitohain11:48
Code POST Python

import requests

def send_post_request():
    url = "https://jsonplaceholder.typicode.com/users&quot;
    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Main St",
            "suite": "Apt. 1",
            "city": "Anytown",
            "zipcode": "12345",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-555-555-5555",
        "website": "johndoe.com",
        "company": {
            "name": "Doe Inc.",
            "catchPhrase": "Innovate the Future",
            "bs": "business solutions"
        }
    }

    try:
        # Envoyer une requête POST avec les données
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        # Afficher la réponse du serveur
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête POST : {e}")
        return None

# Appel de la fonction
if __name__ == "__main__":
    response = send_post_request()
    if response:
        print("Réponse de l'API :", response)

Tsanta Randriatsitohain11:49
Code GET Python

import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users&quot;
    try:
        # Envoyer une requête GET à l'API
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        # Convertir la réponse en JSON
        users = response.json()
        return users
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête GET : {e}")
        return None

# Appel de la fonction et affichage des utilisateurs
if __name__ == "__main__":
    users = fetch_users()
    if users:
        print("Liste des utilisateurs :")
        for user in users:
            print(f"- {user['name']} (Email : {user['email']})")

Tsanta Randriatsitohain12:07
Code PUT Python

import requests

def update_user(user_id, updated_data):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        # Envoyer une requête PUT avec les données mises à jour
        response = requests.put(url, json=updated_data)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        return response.json()  # Retourne la réponse JSON
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête PUT : {e}")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    user_id = 1  # ID de l'utilisateur à mettre à jour
    updated_data = {
        "name": "Jane Doe",
        "username": "janedoe",
        "email": "janedoe@example.com",
        "address": {
            "street": "456 Elm St",
            "suite": "Apt. 2",
            "city": "Othertown",
            "zipcode": "54321",
            "geo": {
                "lat": "-45.3159",
                "lng": "82.1496"
            }
        },
        "phone": "1-555-555-1234",
        "website": "janedoe.com",
        "company": {
            "name": "Doe Consulting",
            "catchPhrase": "Empower the Future",
            "bs": "consulting solutions"
        }
    }

    # Envoyer la requête PUT
    response = update_user(user_id, updated_data)
    if response:
        print("Réponse de l'API :", response)