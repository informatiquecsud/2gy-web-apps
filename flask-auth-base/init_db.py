# init_db.py
import sqlite3

DATABASE_NAME = 'database.db'

def init_db():
    """Initialise la base de données en exécutant le schéma SQL."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        with open('schema.sql', 'r') as f:
            cursor.executescript(f.read())
        conn.commit()
        print("Base de données initialisée avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'initialisation de la base de données : {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    init_db()