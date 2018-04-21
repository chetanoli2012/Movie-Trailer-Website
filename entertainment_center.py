import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#open(toy_story.trailer_youtube_url);
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

interstellar = media.Movie("Interstellar",
                           "With our time on Earth coming to an end, a team of explorers undertakes"+
                           "the most important mission in human history: traveling beyond this galaxy" +
                           "to discover whether mankind has a future among the stars",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

ragnarok = media.Movie("Thor: Ragnarok",
                       "Imprisoned on the other side of the universe, the mighty Thor finds himself"+
                       "in a deadly gladiatorial contest that pits him against the" +
                       "Hulk, his former ally and fellow Avenger.",
                       "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                       "https://www.youtube.com/watch?v=ue80QwXMRHg")

civilwar = media.Movie("Captain America: Civil War",
                       "Friction arises between the superheroes when one group supports the government's" +
                       "decision to implement a law to control their powers while the other opposes it.",
                       "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                       "https://www.youtube.com/watch?v=dKrVegVI0Us")

homecoming = media.Movie("Spider-Man: Homecoming",
                         "Thrilled by his experience with the Avengers, young Peter Parker returns home to"+
                         "live with his Aunt May under the watchful eye of mentor Tony.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                         "https://www.youtube.com/watch?v=DiTECkLZ8HM")

movies= [toy_story, avatar, interstellar, ragnarok, civilwar, homecoming]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)







