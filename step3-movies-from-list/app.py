# Importation de Flask
from flask import Flask
from random import randint
from db import *

# Création de l'application Flask
app = Flask(__name__)



# Route qui affiche une liste de tâches à effectuer
@app.route('/tasks')
def tasks():
    tasks_html = ul(tasks_data)
    print(tasks_html)
    return render_template('layout.html', title='Liste des tâches', content=tasks_html)

# Définition de la route principale
@app.route('/')
def hello():
    content = '''
    <h3>Bienvenue sur notre application Flask !</h3>
    <p>Cette application vous permet de gérer vos tâches.</p>
    <p>Utilisez le lien ci-dessous pour voir la liste des tâches.</p>
    <a href="tasks">Voir les tâches</a>
    '''
    return render_template('layout.html', title='Accueil', content=content)


# Lancement de l'application Si le script est exécuté directement, l'application
# sera lancée sur le serveur de développement intégré de Flask en écoutant sur
# un port aléatoire entre 8001 et 8999.
if __name__ == '__main__':
    port = randint(8001, 8999)
    app.run(debug=True, host='0.0.0.0', port=port)
