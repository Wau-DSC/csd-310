import mysql.connector as sql
from mysql.connector import errorcode as errors

cfg = {
  "user":"movies_user",
  "password":"popcorn",
  "host":"127.0.0.1",
  "database":"movies",
  "raise_on_warnings":True
}

def exec_and_print(db,query,*header):#Runs query and prints formatted output
  cursor = db.cursor()
  cursor.execute(query)
  result = cursor.fetchall()
  for x in result:
    i = 0
    for y in x:
      print(header[i]+": "+str(y)) #The fact that python requires this string cast to be done explicitly is poor design
      i+=1
    print("")
  print("")

try:
  db = sql.connect(**cfg)
  print("-- DISPLAYING Studio RECORDS --")
  exec_and_print(db,"SELECT * FROM studio;","Studio ID","Studio Name")
  print("-- DISPLAYING Genre RECORDS --")
  exec_and_print(db,"SELECT * FROM genre;","Genre ID","Genre Name")
  print("-- DISPLAYING Short Film RECORDS")#Two hours is not the right cutoff for "short" here.
  exec_and_print(db,
    "SELECT film_name,film_runtime FROM film WHERE film_runtime < 120;",
    "Film  Name","Runtime"
  ) 
  print("-- DISPLAYING Director RECORDS in Order --")
  exec_and_print(db,"SELECT film_name,film_director FROM film ORDER BY film_director;","Film Name","Director") 
except sql.Error as err:
  if err.errno == errors.ER_ACCESS_DENIED_ERROR:
    print("  Access denied, verify that username and password are provided correctly.")
  elif err.errno == errors.ER_BAD_DB_ERROR:
    print("  Specified database does not exist.")
  else: print(err)
finally:
  db.close()
  