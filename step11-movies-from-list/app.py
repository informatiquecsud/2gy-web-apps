

from flask import Flask, render_template

app = Flask(__name__)

movie_fields = ["title", "year"]

# liste de champs
movie_fields = [
    'title', 'year', 'director', 'main_actors', 'rating'
]

# liste de films
movies = [
    ['Fight Club', '1999', 'David Fincher', 'Brad Pitt, Edward Norton', '8.8'],
    ['The Lord of the Rings: The Fellowship of the Ring', '2001', 'Peter Jackson', 'Elijah Wood, Ian McKellen', '8.8'],
    ['Forrest Gump', '1994', 'Robert Zemeckis', 'Tom Hanks, Robin Wright', '8.7'],
    ['Star Wars: Episode V - The Empire Strikes Back', '1980', 'Irvin Kershner', 'Mark Hamill, Harrison Ford', '8.7'],
    ['Inception', '2010', 'Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt', '8.7'],
    ['The Lord of the Rings: The Two Towers', '2002', 'Peter Jackson', 'Elijah Wood, Ian McKellen', '8.7'],
]


@app.route('/')
def index():
    html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Movie List</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h1 class="mt-5">Movie List</h1>
                <table class="table table-striped mt-3">
                    <thead>
                        <tr>
                            <th>{movie_fields}</th>
                        </tr>
                    </thead>
                    <tbody>
                        {movies}
                    </tbody>
                </table>
            </div>
        </body>
        </html>
    """
    return html_template.format(
        movie_fields='</th><th>'.join(movie_fields),
        movies='</tr><tr>'.join(['<td>' + '</td><td>'.join(movie) + '</td></tr>' for movie in movies])
    )
    


if __name__ == '__main__':
    app.run(debug=True)
