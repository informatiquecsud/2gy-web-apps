# Importation de Flask
from flask import Flask
from random import randint

# Importation des données
from db import movie_fields, movie_rows
# Importation des fonctions de génération de HTML
from html import render_template, ul, table

# Création de l'application Flask
app = Flask(__name__)

# Route qui affiche une liste de tâches à effectuer
@app.route('/movies')
def movies():
    '''
    Affiche une liste de films à partir des données fournies.
    '''
    return render_template('layout.html', title="Liste des films", content=table(movie_fields, movie_rows))
    
# Définition de la route principale
@app.route('/')
def hello():
    content = '''
    <h3>Bienvenue sur notre application Flask !</h3>
    <p>Cette application vous permet d'afficher une liste de films.</p>
    <p>Utilisez le lien ci-dessous pour voir la liste de films.</p>
    <a href="/movies">Voir les films</a>
    '''
    return render_template('layout.html', title='Accueil', content=content)


# Lancement de l'application Si le script est exécuté directement, l'application
# sera lancée sur le serveur de développement intégré de Flask en écoutant sur
# un port aléatoire entre 8001 et 8999.
if __name__ == '__main__':
    # Vous devez modifier cela avec le numéro de port qui vous a été attribué
    port = 8013
    app.run(debug=True, host='0.0.0.0', port=port)
