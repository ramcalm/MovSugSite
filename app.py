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
        print(movies)
        if movies[1] != 'Movie not found':
            response = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key=a0baf7fe65087ee95486de5163e616ed&language=en-US'
                '&query="' + movies[0] + '"&page=1')
            print(response.status_code)
            dat = response.json()
            poster = "https://image.tmdb.org/t/p/w185/"+dat["results"][0]["poster_path"]
            rdate = dat["results"][0]["release_date"]
            overview = dat["results"][0]["overview"]
            rating = dat["results"][0]["vote_average"]
            votes = dat["results"][0]["vote_count"]
            print(poster)
            return render_template('res.html', result=movies, poster=poster, rdate=rdate, overview=overview, rating=rating, votes=votes)
        else:

            return render_template('notfound.html', result=movies)


if __name__ == '__main__':
    app.run(debug=True)
