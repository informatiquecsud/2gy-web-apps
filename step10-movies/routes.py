from flask import *
from db import *

def ajouter_routes(app):

    # Exemple de route pour afficher la page d'accueil
    # Dans une route, 1) on se connecte à la base de données 2) on exécute une requête SQL,
    # 3) on récupère les informations et on les passe au template HTML pour les afficher
    @app.route("/")
    def page_accueil():

        # 1) Connexion à la base de données
        db = get_db()

        # 2) Requête SQL

        # Création d'un curseur pour faire la requête
        cursor = db.cursor()

        # Requête SQL
        movies_cursor = cursor.execute("SELECT * FROM movies")

        # Transformation de l'objet movies_cursor de type cursor en liste de tuples avec la fonction fetchall()
        movies = movies_cursor.fetchall()

        # 3) On passe la variable movies au template pour pouvoir l'afficher à l'intérieur
        return render_template("page1.html", movies=movies)
    
    # Ajoutez vos différentes routes ci-dessous
    # ...
