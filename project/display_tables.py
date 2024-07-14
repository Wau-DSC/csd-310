import mysql.connector as sql
from mysql.connector import errorcode as errors

cfg = {
  "user":"movies_user",
  "password":"popcorn",
  "host":"127.0.0.1",
  "database":"wilson",
  "raise_on_warnings":True
}

def getRows(cursor,table):
  cursor.execute("SELECT * FROM "+table)
  return cursor.fetchall()

def getClientNameById(cursor,id):
  cursor.execute("SELECT client_name FROM Client WHERE client_id="+str(id))
  for x in cursor.fetchall():
    return x[0]

def getPrimaryContactByClient(cursor,id):
  cursor.execute("SELECT primary_contact FROM Client WHERE client_id="+str(id))
  for x in cursor.fetchall():
    return x[0]
  return getFirstContactByClientId(cursor,id) #Assume first contact is primary if not specified

def getFirstContactByClientId(cursor,id):
  cursor.execute("SELECT contact_id FROM Contact WHERE client_id="+str(id))
  for x in cursor.fetchall():
    return x[0]

try:
  db = sql.connect(**cfg)
  cursor = db.cursor()
  print("--Displaying CLIENTS--")
  for row in getRows(cursor,"Client"):
    row=list(row)
    print("Client id:",row[0])
    print("Client name:",row[1])
    print("Managed assets: $",row[2])
    print("Date registered: ",row[3])
    if(row[4]==None): row[4]=getFirstContactByClient(cursor,row[0])
    print("Primary contact:",row[4])
    print("")
  print("")
  print("--Displaying CONTACTS--")
  for row in getRows(cursor,"Contact"):
    row=list(row)
    print("Contact id:",row[0])
    print("Client id:",row[1])
    if(row[2]==None): row[2]=getClientNameById(cursor,row[1]) #Assume contact name same as client name if not specified
    print("Contact name:",row[2])
    print("Contact phone:",row[3])
    print("Contact email:",row[4])
    print("Contact address:",row[5])
    print("Contact city:",row[6])
    print("Contact state:",row[7])
    print("")
  print("")
  print("--Displaying TRANSACTIONS--")
  for row in getRows(cursor,"Transaction"):
    row=list(row)
    print("Transaction id:",row[0])
    print("Client id:",row[1])
    print("Transaction type:",row[2])
    print("Transaction date:",row[3])
    print("Transaction amount:",row[4])
    print("Transaction status:",row[5])
    print("Transaction memo:",row[6])
    if(row[7]==None): row[7]=getPrimaryContactByClient(cursor,row[1])#Assume primary contact if no contact specified
    print("Contact id:",row[7])
    print("")
except sql.Error as err:
  if err.errno == errors.ER_ACCESS_DENIED_ERROR:
    print("Access denied, verify that username and password are provided correctly.")
  elif err.errno == errors.ER_BAD_DB_ERROR:
    print("Specified database does not exist.")
  else: print(err)
finally:
  db.close()
