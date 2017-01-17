import webbrowser
# calls builtin webbrowser


class Movie():
    """Class Movie provides a way to store movie related information"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        # creates instance variables
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # implements BIF webbrowser, calls trailer
        webbrowser.open(self.trailer_youtube_url)
