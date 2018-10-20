"""Python file for our movies objects"""
import fresh_tomatoes
import media

def main():
    """Create my movies objects"""
    the_matrix = media.Movie("The Matrix",
                             "A computer hacker learns from mysterious rebels about the true nature of reality.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                             "https://www.youtube.com/watch?v=m8e-FF8MsqU")

    the_last_samurai = media.Movie("The Last Samurai",
                                   "An American military advisor embraces the Samurai culture...",
                                   "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",
                                   "https://www.youtube.com/watch?v=T50_qHEOahQ")

    peaceful_warrior = media.Movie("Peaceful Warrior",
                                   "A chance encounter with a stranger changes the life...",
                                   "https://upload.wikimedia.org/wikipedia/en/9/9c/Peaceful_warrior.jpg",
                                   "https://www.youtube.com/watch?v=gegNMYvY_yg")

    inception = media.Movie("Inception",
                            "A thief who steals corporate secrets through the use of dream...",
                            "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                            "https://www.youtube.com/watch?v=YoHD9XEInc0")

    oblivion = media.Movie("Oblivion",
                           "A veteran assigned to extract Earth's remaining resources begins to question...",
                           "https://upload.wikimedia.org/wikipedia/en/2/2e/Oblivion2013Poster.jpg",
                           "https://www.youtube.com/watch?v=XmIIgE7eSak")

    avengers_iw = media.Movie("Avengers: Infinity War",
                              "The Avengers and their allies must be willing to sacrifice all in an attempt...",
                              "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg ",
                              "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

    # List object referencing my movies objects declared above
    movies = [the_matrix, the_last_samurai, peaceful_warrior, inception, oblivion, avengers_iw]

    # Using fresh tomatoes to open the movies page showing my movies objects from the list above
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()