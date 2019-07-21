import media
#import movie_sort
import fresh_tomatoes
kabir_singh=media.movie("Kabir Singh","https://smedia2.intoday.in/btmt/images/stories/kabir_singh_poster2_660_071919110847.jpg","https://youtu.be/RiANSSgCuJk")

avengers_endgame=media.movie("Avengers End Game","https://images-na.ssl-images-amazon.com/images/I/51I7QOlpVeL.jpg","https://youtu.be/TcMBFSGVi1c")

spiderman_farfromhome=media.movie("Spider Man: Far from home","https://specials-images.forbesimg.com/imageserve/5d14be704c687b00085af34e/960x0.jpg?fit=scale","https://youtu.be/Nt9L1jCKGnE")

movies=[kabir_singh,avengers_endgame,spiderman_farfromhome]

#movie_sort.sort(kabir_singh,avengers_endgame,spiderman_farfromhome)

fresh_tomatoes.open_movies_page(movies)

