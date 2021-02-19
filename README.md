# MovSug

Deployed at: https://moviesug.herokuapp.com/

This project is used to predict movies similar to the user's favorite movie using a Machine Learning.

Here the algorithm used is Cosine_Similarity algorithm which is done on the dataset obtained which is also added in the repository.

After fetching the similar movie based on the Algorithm using TMDB API details regarding the movie is fetched and displayed for the user.


If you want to run it in your local environment locally follow the following steps

1.Clone/Download this repository

2.Replace <YOUR_TMDB_API_KEY> on line 21 in app.py with your api key which you can generate by registering at: https://www.themoviedb.org.

The Movie Database (TMDb) is a popular, user editable database for movies and TV shows.


3.Run the following commands
```
pip install -r requirements.txt
```
```
python app.py
```
4.Change the url in test.py to http://localhost:5000 and you can proceed.

Sample:

<img src="https://i.ibb.co/0KSVyff/op1.png" align="center" width="500px" alt="image">
<br>
<br>
<img src="https://i.ibb.co/XsLffz9/op2.png" align="center" width="500px" alt="image">

