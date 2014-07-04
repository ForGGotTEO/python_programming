import fresh_tomatoes
import media

tfios = media.Movie("The Fault In Our Stars",
                     "Not your average love story.",
                     "http://static2.hypable.com/wp-content/uploads/2013/12/fault-in-our-stars-movie-poster-full.jpg",
                     "http://www.youtube.com/watch?v=9ItBvH5J6ss&feature=kp")
#print(tfios.storyline)

xmen = media.Movie("X-men: Days Of Future Past",
                    "A story about mutants, their future, and their past.",
                    "http://www.eonline.com/eol_images/Entire_Site/2014224/rs_634x939-140324091106-634.jennifer-lawrence-x-men.ls.32414.jpg",
                    "http://www.youtube.com/watch?v=pK2zYHWDZKo")
#xmen.show_trailer()

wdmc = media.Movie("What Dreams May Come",
                    "A tragic story of a family in despair, that is reunited once more",
                    "https://www.movieposter.com/posters/archive/main/106/MPW-53359",
                    "http://www.youtube.com/watch?v=RmZ-FuBThuQ")
#wdmc.show_trailer()

ratatouille = media.Movie("Ratatouille",
                            "A story of a rat in France that wants to become a chef.",
                            "http://img3.wikia.nocookie.net/__cb20130930090447/moviepedia/de/images/2/29/Poster-de-ratatouille.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")

potc = media.Movie("Pirates Of The Carribean",
                    "A story of pirates.",
                    "http://static.dramastyle.com/images/3/3/6758/Pirates-of-the-Caribbean:-The-Curse-of-the-Black-Pearl__5.jpg",
                    "https://www.youtube.com/watch?v=0Z1XpfbuZOA")

harry_potter = media.Movie("Harry Potter And The Deathly Hallows Part 2",
                            "A story of a boy, a wizard, and a lot of death.",
                            "http://www.schizopolitan.com/wp-content/uploads/2011/07/dh-part-2-official-poster-high-res.jpg",
                            "https://www.youtube.com/watch?v=5NYt1qirBWg")

movies = [tfios, xmen, wdmc, ratatouille, potc, harry_potter]


fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
