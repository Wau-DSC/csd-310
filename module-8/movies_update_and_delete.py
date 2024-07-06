import mysql.connector as sql
from mysql.connector import errorcode as errors

cfg = {
  "user":"movies_user",
  "password":"popcorn",
  "host":"127.0.0.1",
  "database":"movies",
  "raise_on_warnings":True
}

def show_films(cursor,title):
  cursor.execute(
     """SELECT film_name,film_director,genre_name,studio_name FROM film
       INNER JOIN genre ON film.genre_id=genre.genre_id
       INNER JOIN studio ON film.studio_id=studio.studio_id;"""
  )
  films = cursor.fetchall()
  print("\n -- {} --".format(title))
  for film in films:
    print("Film Name: {}\nDirector:{}\nGenre Name: {}\nStudio Name:{}\n".format(
      film[0],film[1],film[2],film[3]
    ))

try:
  db = sql.connect(**cfg)
  cursor = db.cursor()
  show_films(cursor,"DISPLAYING FILMS")
  cursor.execute("INSERT INTO film VALUES (4,'FilmTitle',1806,15,'FilmDirector',1,1)")
  show_films(cursor,"DISPLAYING FILMS AFTER INSERT")
  cursor.execute("UPDATE film SET genre_id=1 WHERE film_id=2")
  show_films(cursor,"DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")
  cursor.execute("DELETE FROM film WHERE film_name='Gladiator'")
  show_films(cursor,"DISPLAYING FILMS AFTER DELETE")
except sql.Error as err:
  if err.errno == errors.ER_ACCESS_DENIED_ERROR:
    print("Access denied, verify that username and password are provided correctly.")
  elif err.errno == errors.ER_BAD_DB_ERROR:
    print("Specified database does not exist.")
  else: print(err)
finally:
  db.close()
  