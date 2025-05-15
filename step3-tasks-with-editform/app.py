# Importation de Flask
from flask import Flask
from random import randint

# Importation des fonctions de génération de HTML
from html_builder import render_template, ul

# Création de l'application Flask
app = Flask(__name__)

# Données manipulées par l'application
tasks_data = [
    'Apprendre Python',
    'Apprendre Flask',
    'Créer une application Web'
]

# Route qui affiche une liste de tâches à effectuer
@app.route('/tasks')
def tasks():
    tasks_html = ul(tasks_data)
    return render_template('layout.html', title='Liste des tâches', content=tasks_html)

# Définition de la route principale
@app.route('/')
def hello():
    content = render_template('welcome.html')
    return render_template('layout.html', title='Accueil', content=content)


# Lancement de l'application Si le script est exécuté directement, l'application
# sera lancée sur le serveur de développement intégré de Flask en écoutant sur
# un port aléatoire entre 8001 et 8999.
if __name__ == '__main__':
    port = randint(8001, 8999)
    app.run(debug=True, host='0.0.0.0', port=port)
