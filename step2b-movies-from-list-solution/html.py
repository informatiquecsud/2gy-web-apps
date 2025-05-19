import os

def render_template_str(template_string, **context):
    for key, value in context.items():
        template_string = template_string.replace('{{ ' + key + ' }}', str(value))
    return template_string

def render_template(filename, **context):
    """
    Charge un fichier de modèle HTML et le renvoie sous forme de chaîne.
    """
    template_file = os.path.join('templates', filename)
    html_template = ''
    with open(template_file, 'r') as file:
        html_template = file.read()
    return render_template_str(html_template, **context)

def ul(items):
    """
    Crée une liste HTML à partir d'une liste d'éléments.
    """
    html = '<ul>'
    for item in items:
        html += f'<li>{item}</li>'
    html += '</ul>'
    return html


def tr(data, cell='td'):
    html = '<tr>'
    for d in data:
        html += f'<{cell}>{d}</{cell}>'
    html += '</tr>'
    return html


def table(headers, rows):
    html_template = '''
        <table class="table table-striped table-hover table-bordered">
            <thead class="table-dark">
                {{ headers }}
            </thead>
            <tbody>
                {{ table_body }}
            </tbody>
        </table>
    '''
    headers_html = tr(headers, cell='th')
    body_html = ''
    for row in rows:
        body_html += tr(row, cell='td')

    return render_template_str(
        html_template, 
        headers=headers_html, 
        table_body=body_html
    )