import webbrowser

# Class
class Movie():
    # Constructor
    def __init__(self, title, storyline, image, trailer):
        # Instance Variables
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    # Instance Method to show trailer using webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer)
