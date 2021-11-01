from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
movies_genres = db.Table('movies_genres',
                         db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
                         db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True))

movies_actors = db.Table('movies_actors',
                         db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
                         db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True))


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date)

    def __repr__(self):
        return f'{self.title}'


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    movies = db.relationship('Movie', secondary=movies_genres, lazy='subquery', backref=db.backref('genres', lazy=True))

    def __repr__(self):
        return f'{self.name}'


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    movies = db.relationship('Movie', secondary=movies_actors, lazy='subquery', backref=db.backref('actors', lazy=True))

    def __repr__(self):
        return f'{self.name}'
