from flask import Flask, render_template, request
from movie_recommendation import similar_movies

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        movies=similar_movies(result["movie"])
        return render_template('res.html', result=movies)


if __name__ == '__main__':
    app.run(debug=True)
