import sqlite3
from flask import g

# Permet de récupérer la connexion à la base de données
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
        db.row_factory = sqlite3.Row
    return db

# Permet de donner un accès à la db à chaque requête et de fermer la connexion en cas de problème
def initialiser_db(app):
    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()