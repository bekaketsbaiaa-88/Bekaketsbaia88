import json
from dataclasses import dataclass, field, asdict


@dataclass
class Movie:
    title: str
    year: int = 2000
    rating: float = 0.0
    genres: list = field(default_factory=list)

    def __post_init__(self):
        if self.rating < 0 or self.rating > 10:
            raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")


def best_movies(movies, min_rating):
    good = [movie for movie in movies if movie.rating >= min_rating]
    return sorted(good, key=lambda movie: movie.rating, reverse=True)


movie1 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
movie2 = Movie("გზა", 2020, 7.5)
movie3 = Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"])

print(movie1)
print(movie1 == Movie("მონანიება", 1984, 9.1, ["დრამა"]))

movie2.genres.append("კომედია")
print(movie2.genres, movie3.genres)

for movie in best_movies([movie1, movie2, movie3], 8):
    print(movie.title, movie.rating)

print(json.dumps(asdict(movie1), ensure_ascii=False))

try:
    Movie("ცუდი", 2000, 11)
except ValueError as error:
    print("შეცდომა:", error)
