import mysql.connector as sql
from mysql.connector import errorcode as errors

cfg = {
  "user":"movies_user",
  "password":"popcorn",
  "host":"127.0.0.1",
  "database":"wilson",
  "raise_on_warnings":True
}

try:
  db = sql.connect(**cfg)
  cursor = db.cursor()
  print("New client registrations by month (past 6 months):")
  print("--------------------------------------------------")
  cursor.execute(
    """
      SELECT YEAR(date_registered),MONTH(date_registered),COUNT(MONTH(date_registered)) FROM client
      WHERE TIMESTAMPDIFF(month,LAST_DAY(date_registered),LAST_DAY(CURDATE())) BETWEEN 1 AND 7
      GROUP BY YEAR(date_registered),MONTH(date_registered) ORDER BY YEAR(date_registered),MONTH(date_registered)
    """
  )
  rows_fetched = cursor.fetchall()
  cursor.execute("SELECT YEAR(DATE_SUB(LAST_DAY(CURDATE()),INTERVAL 6 MONTH)),MONTH(DATE_SUB(LAST_DAY(CURDATE()),INTERVAL 6 MONTH))")
  month = cursor.fetchall()[0]
  month = (int(month[0]),int(month[1]))
  i = 0
  #Print values, filling in zeroes for missing entries
  for j in range(6):
    if i < len(rows_fetched) and (int(rows_fetched[i][0]),int(rows_fetched[i][1]))==month:
      print("%02d/%d: %s" % (month[1],month[0],rows_fetched[i][2]))
      i+=1
    else:
      print("%02d/%d: 0" % (month[1],month[0]))
    month = (month[0]+1 if month[1]==12 else month[0],1 if month[1]==12 else month[1]+1) #Python does ternarys wrong
except sql.Error as err:
  if err.errno == errors.ER_ACCESS_DENIED_ERROR:
    print("Access denied, verify that username and password are provided correctly.")
  elif err.errno == errors.ER_BAD_DB_ERROR:
    print("Specified database does not exist.")
  else: print(err)
finally:
  db.close()
