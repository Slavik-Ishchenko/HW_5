from flask import Blueprint, render_template
from models import Movie, Genre, Actor
first_route = Blueprint('first', __name__, template_folder='templates')


@first_route.route("/")
def index():
    movies = Movie.query.all()
    genres = Genre.query.all()
    actors = Actor.query.all()
    return render_template('index.html', movies=movies, genres=genres, actors=actors)
