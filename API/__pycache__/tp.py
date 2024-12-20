from flask import Flask, jsonify, request
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

#from flask_talisman import Talisman

app = Flask(__name__)
#Talisman (app)

# Configuration de la base de données
DATABASE_URL = "sqlite:///employees.db"
engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

# Définir la table des employés
employees_table = Table(
    'employees', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('Nom', String),
    Column('Prenom', String),
    Column('Fonction', String),
    Column('Anciennete', Integer)
)

# Créer la table si elle n'existe pas
metadata.create_all(engine)

# Routes API
@app.route('/employees', methods=['GET'])
def get_employees():
    with engine.begin() as connection:
        query = employees_table.select()
        result = connection.execute(query)
        employees = [row._asdict() for row in result]
        return jsonify(employees)

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    with engine.begin() as connection:
        query = employees_table.select().where(employees_table.c.id == employee_id)
        result = connection.execute(query).fetchone()
        if result:
            return jsonify(result._asdict())
        else:
            return jsonify({'error': 'Employé non trouvé'}), 404

@app.route('/employees/add', methods=['POST'])
def add_employee():
    data = request.json  # Récupérer les données envoyées au format JSON
    with engine.begin() as connection:
        query = employees_table.insert().values(
            Nom=data['Nom'],
            Prenom=data['Prenom'],
            Fonction=data['Fonction'],
            Anciennete=data['Anciennete']
        )
        result = connection.execute(query)
        return jsonify({'id': result.inserted_primary_key[0]}), 201


@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json  # Récupère les données JSON envoyées dans la requête
    with engine.begin() as connection:
        # Crée une requête de mise à jour
        update_query = employees_table.update().where(employees_table.c.id == id).values(
            Nom=data.get('Nom'),
            Prenom=data.get('Prenom'),
            Fonction=data.get('Fonction'),
            Anciennete=data.get('Anciennete')
        )
        result = connection.execute(update_query)

        # Vérifie si un enregistrement a été mis à jour
        if result.rowcount > 0:
            return jsonify({"message": "Employé mis à jour avec succès"}), 200
        else:
            return jsonify({"error": "Employé introuvable"}), 404
        
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    with engine.begin() as connection:
        # Crée une requête de suppression
        delete_query = employees_table.delete().where(employees_table.c.id == id)
        result = connection.execute(delete_query)

        # Vérifie si un enregistrement a été supprimé
        if result.rowcount > 0:
            return jsonify({"message": "Employé supprimé avec succès"}), 200
        else:
            return jsonify({"error": "Employé introuvable"}), 404

if __name__ == '__main__':
    app.run(debug=True)

