import os


def render_template_str(template_string, **context):
    """
    Remplace tous les "blancs" {{ blanc }} par les valeurs présentes dans le
    dictionnaire ``context``. La chaîne de caractères ``template_string``
    représente une sorte de "texte à trous" où les "trous" peuvent être remplis

    >>> render_template_str('Bonjour {{ name }}', name='Alice')
    'Bonjour Alice'
    >>> render_template_str('<h1>{{ title }}</h1><p>{{ message }}</p>', title='Message de test', message='Ceci est un test')
    '<h1>Message de test</h1><p>Ceci est un test</p>'
    """
    for key, value in context.items():
        template_string = template_string.replace("{{ " + key + " }}", str(value))
    return template_string


def render_template(filename, **context):
    """
    Charge un template HTML depuis le fichier `filename` présent dans le dossier
    ``templates`` et remplace les "blancs" {{ blanc }} par les valeurs présentes
    dans le dictionnaire ``context``.
    """
    template_file = os.path.join("templates", filename)
    html_template = ""
    with open(template_file, "r") as file:
        html_template = file.read()
    return render_template_str(html_template, **context)


def ul(items):
    """
    Crée une liste HTML à partir d'une liste d'éléments.
    
    >>> ul(['Pommes', 'Bananes', 'Fraises'])
    '<ul><li>Pommes</li><li>Bananes</li><li>Fraises</li></ul>'
    """
    html = "<ul>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ul>"
    return html


def tr(data, cell="td"):
    """
    Crée une ligne de tableau HTML à partir d'une liste de données. Chaque
    élément de la liste sera contenu dans une cellule de type `cell` (doit 'td'
    pour les cellules de données du tableau, soit 'th' pour les cellules de
    l'en-tête du tableau).
    """
    html = "<tr>"
    for d in data:
        html += f"<{cell}>{d}</{cell}>"
    html += "</tr>"
    return html


def table(headers, rows):
    """
    Génère un tableau HTML à partir d'une liste d'en-têtes `headers` et d'une
    liste de lignes `rows` (liste de listes). Les en-têtes seront affichés dans
    la première ligne du tableau et chaque ligne de `rows` sera affichée dans une
    ligne du tableau.
    Les en-têtes seront affichés dans des cellules de type `th` et les autres
    cellules dans des cellules de type `td`.
    >>> headers = ['Titre', 'Année']
    >>> rows = [
    ...     ['Inception', 2010],
    ...     ['Interstellar', 2014],
    ...     ['Dunkirk', 2017]
    ... ]
    >>> print(table(headers, rows))
    <table class="table table-striped table-hover table-bordered">
        <thead class="table-dark">
            <tr><th>Titre</th><th>Année</th></tr>
        </thead>
        <tbody>
            <tr><td>Inception</td><td>2010</td></tr>
            <tr><td>Interstellar</td><td>2014</td></tr>
            <tr><td>Dunkirk</td><td>2017</td></tr>
        </tbody>
    </table>
    """
    html_template = """
        <table class="table table-striped table-hover table-bordered">
            <thead class="table-dark">
                {{ headers }}
            </thead>
            <tbody>
                {{ table_body }}
            </tbody>
        </table>
    """
    headers_html = tr(headers, cell="th")
    body_html = ""
    for row in rows:
        body_html += tr(row, cell="td")

    return render_template_str(
        html_template, headers=headers_html, table_body=body_html
    )


if __name__ == "__main__":
    # Test de la fonction render_template_str
    import doctest

    doctest.testmod()

    print(render_template_str("Bonjour {{ name }}", name="Alice"))
    print(
        render_template_str(
            "<h1>{{ title }}</h1><p>{{ message }}</p>",
            title="Message de test",
            message="Ceci est un test",
        )
    )

    # Test de la fonction ul
    print(ul(["Item 1", "Item 2", "Item 3"]))

    # Test de la fonction tr
    print(tr(["Cellule 1", "Cellule 2", "Cellule 3"]))
    print(tr(["En-tête 1", "En-tête 2"], cell="th"))

    # Test de la fonction table
    headers = ["Titre", "Année"]
    rows = [["Inception", 2010], ["Interstellar", 2014], ["Dunkirk", 2017]]
    print(table(headers, rows))
