"""Python file for our movies objects"""
import fresh_tomatoes
import media


def main():
    """Create my movies objects"""
    the_matrix = media.Movie("The Matrix",
                             "A computer hacker learns from mysterious ...",
                             "https://upload.wikimedia.org/wikipedia/en/c/"
                             "c1/The_Matrix_Poster.jpg",
                             "https://www.youtube.com/watch?v=m8e-FF8MsqU")

    the_last_samurai = media.Movie("The Last Samurai",
                                   "An American military advisor embraces ...",
                                   "https://upload.wikimedia.org/wikipedia/en"
                                   "/c/c6/The_Last_Samurai.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=T50_qHEOahQ")

    peaceful_warrior = media.Movie("Peaceful Warrior",
                                   "A chance encounter with a stranger ...",
                                   "https://upload.wikimedia.org/wikipedia/en/"
                                   "9/9c/Peaceful_warrior.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=JvENjJI-7r0")

    inception = media.Movie("Inception",
                            "A thief who steals corporate secrets through ...",
                            "https://upload.wikimedia.org/wikipedia/en/2/2e/"
                            "Inception_%282010%29_theatrical_poster.jpg",
                            "https://www.youtube.com/watch?v=YoHD9XEInc0")

    oblivion = media.Movie("Oblivion",
                           "A veteran assigned to extract Earth's ...",
                           "https://upload.wikimedia.org/wikipedia/en/2/2e/"
                           "Oblivion2013Poster.jpg",
                           "https://www.youtube.com/watch?v=XmIIgE7eSak")

    avengers_iw = media.Movie("Avengers: Infinity War",
                              "The Avengers and their allies must ...",
                              "https://upload.wikimedia.org/wikipedia/en/4/4d/"
                              "Avengers_Infinity_War_poster.jpg ",
                              "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

    # List object referencing my movies objects declared above
    movies = [the_matrix, the_last_samurai, peaceful_warrior, inception,
              oblivion, avengers_iw]

    # Using fresh tomatoes to open the page showing my list of movies objects
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
