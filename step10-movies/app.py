from flask import Flask
from routes import *
from db import *
import os

# Fonction automatiquement appelée par le framework Flask lors de l'exécution de la commande python -m flask run permettant de lancer le projet
# La fonction retourne une instance de l'application créée
def create_app():

    # Crée l'application Flask
    app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())

    # On retourne l'instance de l'application Flask
    return app

# Création de l'application
app = create_app()

# Initialisation de la base de donnée
initialiser_db(app)

# Ajout des routes à l'application
ajouter_routes(app)

# Lorsque le fichier est exécuté, démarrage de l'application
if __name__ == "__main__":
    app.run(debug=True)