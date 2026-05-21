from fastapi import FastAPI

app = FastAPI()

movies =[
        {
        "id": 1,
        "title": "Avengers Endgame",
        "genre": "action",
        "rating": 9.0
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "sci-fi",
        "rating": 9.5
    },
    {
        "id": 3,
        "title": "John Wick",
        "genre": "action",
        "rating": 8.7
    },
    {
        "id": 4,
        "title": "The Conjuring",
        "genre": "horror",
        "rating": 8.2
    },
    {
        "id": 5,
        "title": "3 Idiots",
        "genre": "comedy",
        "rating": 9.1
    },
    {
        "id": 6,
        "title": "Inception",
        "genre": "sci-fi",
        "rating": 9.3
    }
]

#Home route
@app.get('/')
def home():
    return "Movies API"

#Movies by genre
@app.get('/movies')
def get_movies(genre: str = None):
    if genre:
        filtered_movies = []
        for movie in movies:
            if movie['genre'].lower() == genre.lower():
                filtered_movies.append({
                    "title": movie['title'],
                    "rating": movie['rating']})
        return filtered_movies
    return movies


