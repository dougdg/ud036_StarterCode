"""Media file class for our movie class and it's properties."""
import webbrowser

class Movie():
    """Movie class to instantiate movie objects and properties"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Constructor that initialises the Movie class and it's variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url =  poster_image
        self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
        """Function that plays the trailer by using the web browser."""
        webbrowser.open(self.trailer_youtube_url)