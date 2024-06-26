import mysql.connector as sql
from mysql.connector import errorcode as errors

cfg = {
  "user":"movies_user",
  "password":"popcorn",
  "host":"127.0.0.1",
  "database":"movies",
  "raise_on_warnings":True
}

try:
  db = sql.connect(**cfg)
  print("\n  User {} connected to host {} with database {}".format(cfg["user"],cfg["host"],cfg["database"]))
  input("\n\n  Press any key to continue...")
except sql.Error as err:
  if err.errno == errors.ER_ACCESS_DENIED_ERROR:
    print("  Access denied, verify that username and password are provided correctly.")
  elif err.errno == errors.ER_BAD_DB_ERROR:
    print("  Specified database does not exist.")
  else: print(err)
finally:
  db.close()
  