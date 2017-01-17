import fresh_tomatoes
import media
# Calls init function in Movie class, makes space/memory for new instance

# Each movie is linked to class Movie where listed properties are defined
the_princess_bride = media.Movie("The Princess Bride",
                                 "https://s-media-cache-ak0.pinimg.com/originals/b6/8d/0d/b68d0d9c5a2fca3d67118d34fe53c6b7.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=njZBYfNpWoE")

the_martian = media.Movie("The Martian",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

the_lego_movie = media.Movie("The Lego Movie",
                             "http://www.impawards.com/2014/posters/lego_movie_ver9_xlg.jpg",  # noqa
                             "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

christmas_vacation = media.Movie("Christmas Vacation",
                                 "https://fanart.tv/fanart/movies/5825/movieposter/national-lampoons-christmas-vacation-55ad517500dbc.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=NBTTipJX-h4",)

arrival = media.Movie("Arrival",
                      "http://ichef.bbci.co.uk/news/660/cpsprodpb/48CA/production/_90843681_890a8bd8-6501-11e6-aefa-e8609c477948_486x.jpg",  # noqa
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")  # noqa

interstellar = media.Movie("Interstellar",
                           "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",  # noqa
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

# Declares list of objects under movies
movies = [the_princess_bride, the_martian, the_lego_movie, christmas_vacation, arrival, interstellar]

# calls method fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
