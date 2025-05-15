def render_template(filename, **kwargs):
    """
    Charge un fichier de modèle HTML et le renvoie sous forme de chaîne.
    """
    html = ''
    with open(filename, 'r') as file:
        html = file.read()
    for key, value in kwargs.items():
        html = html.replace('{{ ' + key + ' }}', str(value))
    return html

def ul(items):
    """
    Crée une liste HTML à partir d'une liste d'éléments.
    """
    html = '<ul>'
    for item in items:
        html += f'<li>{item}</li>'
    html += '</ul>'
    return html