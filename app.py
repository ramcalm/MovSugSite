from flask import Flask, render_template, request
from movie_recommendation import similar_movies
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        movies = similar_movies(result["movie"])
        if movies[1] != 'Movie not found':
            response = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key=<<YOUR_API_KEY>>&language=en-US'
                '&query="' + movies[0] + '"&page=1')
            dat = response.json()
            poster = "https://image.tmdb.org/t/p/w185/"+dat["results"][0]["poster_path"]
            rdate = dat["results"][0]["release_date"]
            overview = dat["results"][0]["overview"]
            rating = dat["results"][0]["vote_average"]
            votes = dat["results"][0]["vote_count"]
            return render_template('res.html', result=movies, poster=poster, rdate=rdate, overview=overview, rating=rating, votes=votes)
        else:

            return render_template('notfound.html', result=movies)


if __name__ == '__main__':
    app.run(debug=True)
