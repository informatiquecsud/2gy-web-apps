# Importation de Flask
from flask import Flask
from random import randint

# Création de l'application Flask
app = Flask(__name__)

# Route qui affiche une liste de tâches à effectuer
@app.route('/tasks')
def tasks():
    return '''
    <ul>
        <li>Apprendre Python</li>
        <li>Apprendre Flask</li>
        <li>Créer une application Web</li>
    </ul>
    '''

# Définition de la route principale
@app.route('/')
def hello():
    return 'Hello World!'

# Route qui dit bonjour à l'utilisateur
@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

# Lancement de l'application Si le script est exécuté directement, l'application
# sera lancée sur le serveur de développement intégré de Flask en écoutant sur
# un port aléatoire entre 8001 et 8999.
if __name__ == '__main__':
    port = randint(8001, 8999)
    app.run(debug=True, host='0.0.0.0', port=port)
