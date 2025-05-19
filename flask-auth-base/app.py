# app.py
import sqlite3
from random import randint

from flask import Flask, render_template, request, redirect, url_for, session, g, flash
from werkzeug.security import generate_password_hash, check_password_hash
import functools # Pour le décorateur login_required


# Configuration de l'application
app = Flask(__name__)
app.config['SECRET_KEY'] = '1KEoXu9WxSNbF14fSlURVx0ck' # Changez ceci !
app.config['DATABASE'] = 'database.db'


# --- Gestion de la base de données ---
def get_db():
    """Ouvre une nouvelle connexion à la base de données si aucune n'existe pour le contexte actuel."""
    if 'db' not in g:
        try:
            g.db = sqlite3.connect(app.config['DATABASE'])
            g.db.row_factory = sqlite3.Row # Permet d'accéder aux colonnes par nom
        except sqlite3.Error as e:
            flash(f"Erreur de connexion à la base de données: {e}", "danger")
            return None
    return g.db

@app.teardown_appcontext
def close_db(error=None):
    """Ferme la connexion à la base de données à la fin de la requête."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

# --- Décorateur pour les routes nécessitant une connexion ---
def login_required(view):
    """
    Décorateur qui redirige vers la page de connexion si l'utilisateur n'est pas connecté.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            flash("Vous devez être connecté pour accéder à cette page.", "warning")
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view

# --- Routes ---
@app.route('/')
def index():
    """Page d'accueil."""
    if 'user_id' in session:
        db = get_db()
        if not db:
            return render_template('index.html', username=None)
        try:
            user_cursor = db.execute('SELECT username FROM users WHERE id = ?', (session['user_id'],))
            user = user_cursor.fetchone()
            if user:
                return render_template('index.html', username=user['username'])
        except sqlite3.Error as e:
            flash(f"Erreur lors de la récupération des informations utilisateur: {e}", "danger")
        
    return render_template('index.html', username=None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Page d'enregistrement."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        error = None

        if not username:
            error = "Le nom d'utilisateur est requis."
        elif not password:
            error = "Le mot de passe est requis."
        elif password != confirm_password:
            error = "Les mots de passe ne correspondent pas."

        if error is None:
            db = get_db()
            if not db:
                flash("Erreur de base de données, impossible de s'enregistrer.", "danger")
                return render_template('register.html')
            try:
                # Vérifier si l'utilisateur existe déjà
                user_exists_cursor = db.execute('SELECT id FROM users WHERE username = ?', (username,))
                if user_exists_cursor.fetchone() is not None:
                    error = f"L'utilisateur {username} existe déjà."
                else:
                    # Hasher le mot de passe avant de le stocker
                    password_hash = generate_password_hash(password)
                    db.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
                    db.commit()
                    flash('Enregistrement réussi ! Vous pouvez maintenant vous connecter.', 'success')
                    return redirect(url_for('login'))
            except sqlite3.IntegrityError: # Devrait être attrapé par la vérification ci-dessus, mais par sécurité
                 error = f"L'utilisateur {username} existe déjà (IntegrityError)."
            except sqlite3.Error as e:
                error = f"Erreur de base de données lors de l'enregistrement : {e}"
        
        if error:
            flash(error, 'danger')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Page de connexion."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        db = get_db()

        if not db:
            flash("Erreur de base de données, impossible de se connecter.", "danger")
            return render_template('login.html')

        try:
            user_cursor = db.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = user_cursor.fetchone()

            if user is None:
                error = "Nom d'utilisateur incorrect."
            elif not check_password_hash(user['password_hash'], password):
                error = "Mot de passe incorrect."
            
            if error is None:
                # Connexion réussie, stocker l'ID de l'utilisateur dans la session
                session.clear()
                session['user_id'] = user['id']
                session['username'] = user['username'] # Optionnel, pour un accès facile
                flash('Connexion réussie !', 'success')
                return redirect(url_for('index'))
        except sqlite3.Error as e:
            error = f"Erreur de base de données lors de la connexion : {e}"

        if error:
            flash(error, 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    """Déconnexion de l'utilisateur."""
    session.clear()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('login'))

@app.route('/profile')
@login_required # Protège cette route
def profile():
    """Page de profil utilisateur (exemple de page protégée)."""
    # Nous pourrions récupérer plus d'infos sur l'utilisateur ici si nécessaire
    return render_template('profile.html', username=session.get('username'))

if __name__ == '__main__':
    port = 8011
    app.run(debug=True, host="localhost", port=port)