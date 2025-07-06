def show_favourites(movies):
    for title in movies:
        print(f"Dzięki za polecenie: ")

# Tworzenie listy
favourite_movies = []

for i in range(3):
    movie = input(f"Podaj film nr {i+1}: ")
    favourite_movies.append(movie)

# Wywołanie funkcji
show_favourites(favourite_movies)