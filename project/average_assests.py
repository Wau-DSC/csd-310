import mysql.connector 
import pandas as pd

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='wilson2',
    password='pass123',
    database='wilson'
)

# Create a cursor object
cursor = conn.cursor()

# Execute the query
query = "SELECT AVG(managed_assets) AS average_assets FROM Client;"
cursor.execute(query)

# Fetch the data
data = cursor.fetchone()

# Load data into a DataFrame
df = pd.DataFrame([data], columns=['Average Assets'])

# Print the DataFrame
print(df)

# Close the cursor and connection
cursor.close()
conn.close()
