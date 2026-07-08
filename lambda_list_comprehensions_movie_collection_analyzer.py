def analyze_movies(movies: list[dict]) -> dict:
    titles = [movie["title"] for movie in movies]

    titles_after_2000 = [movie["title"] for movie in movies if movie["year"] > 2000]

    titles_upper = [title.upper() for title in titles]

    genres = set([movie["genre"] for movie in movies]) # same as {movie["genre"] for movie in movies}
    
    best_to_worse = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    best_movie = best_to_worse[0]["title"]

    '''oldest_year = movies[0]["year"]
    for movie in movies:
        if movie["year"] < oldest_year:
            oldest_year = movie["year"]
            oldest_movie = movie["title"]''' # is the same as: ↓

    oldest_movie = (min(movies, key=lambda movie: movie["year"]))["title"]

    average_rating = sum([movie["rating"] for movie in movies]) / len(movies)

    return {
        "titles": titles,
        "recent_movies": titles_after_2000,
        "uppercase_titles": titles_upper,
        "genres": genres,
        "sorted_movies": best_to_worse,
        "best_movie": best_movie,
        "oldest_movie": oldest_movie,
        "average_rating": average_rating
    }



movies = [
    {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Sci-Fi"},
    {"title": "Interstellar", "year": 2014, "rating": 8.6, "genre": "Sci-Fi"},
    {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime"},
    {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime"},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action"},
    {"title": "Gladiator", "year": 2000, "rating": 8.5, "genre": "Action"},
]

print(analyze_movies(movies))

'''
Output:
{
    "titles": ...,
    "recent_movies": ...,
    "uppercase_titles": ...,
    "genres": ...,
    "sorted_movies": ...,
    "best_movie": ...,
    "oldest_movie": ...,
    "average_rating": ...
}
'''