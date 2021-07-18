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
        mov = result["movie"];
        print(mov)
        movies = similar_movies(result["movie"])
        if movies[1] != 'Movie not found':
            response = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key=a0baf7fe65087ee95486de5163e616ed&language=en-US'
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

@app.route('/getsimilar', methods=['POST', 'GET'])
def getsimilar():
    if request.method == 'POST':
        result = request.form
        mov = result["movie"];
        print(mov)
        movies = similar_movies(result["movie"])
        if movies[1] != 'Movie not found':
            response = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key=a0baf7fe65087ee95486de5163e616ed&language=en-US'
                '&query="' + movies[0] + '"&page=1')
            dat = response.json()
            return movies
        else:
            return "Movie Not found"
    if request.method == 'GET':
        mov = request.args.get("movie")
        print(mov)
        movies = similar_movies(mov)
        if movies[1] != 'Movie not found':
            response = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key=a0baf7fe65087ee95486de5163e616ed&language=en-US'
                '&query="' + movies[0] + '"&page=1')
            dat = response.json()
            return movies
        else:
            return "Movie Not found"

@app.route('/getinfo', methods=['POST', 'GET'])
def getinfo():
    if request.method == 'POST':
        result = request.form
        mov = result["movie"];
        print(mov)
        movies = similar_movies(result["movie"])
        if movies[1] != 'Movie not found':
            response = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key=a0baf7fe65087ee95486de5163e616ed&language=en-US'
                '&query="' + movies[0] + '"&page=1')
            dat = response.json()
            dat = dat["results"][0]
            del dat["video"]
            del dat["adult"]
            del dat["genre_ids"]
            return dat
        else:
            return "Movie Not Found"
    if request.method == "GET":
        mov = request.args.get("movie")
        print(mov)
        movies = similar_movies(mov)
        if movies[1] != 'Movie not found':
            response = requests.get(
                'https://api.themoviedb.org/3/search/movie?api_key=a0baf7fe65087ee95486de5163e616ed&language=en-US'
                '&query="' + movies[0] + '"&page=1')
            dat = response.json()
            dat = dat["results"][0]
            del dat["video"]
            del dat["adult"]
            del dat["genre_ids"]
            del dat["backdrop_path"]
            del dat["id"]
            del dat["poster_path"]
            return dat
        else:
            return "Movie Not Found"


if __name__ == '__main__':
    app.run(debug=True)
