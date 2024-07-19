import mysql.connector 
from mysql.connector import errorcode as errors
import pandas as pd

try:
# Connect to the database
    conn = mysql.connector.connect(
        host='localhost',
        user='wilson2',
        password='pass123',
        database='wilson'
    )

      # Create a cursor object
    cursor = conn.cursor()

    # Execute the query to get all clients
    cursor.execute("SELECT client_id, client_name, managed_assets FROM Client;")
    clients = cursor.fetchall()

    # Load data into a DataFrame and print
    df_clients = pd.DataFrame(clients, columns=['Client ID', 'Client Name', 'Managed Assets'])
    print("All Client Data:")
    print(df_clients)

    # Execute the query to get min and max managed assets
    query = "SELECT MIN(managed_assets) AS minimum_assets, MAX(managed_assets) AS maximum_assets FROM Client;"
    cursor.execute(query)

    # Fetch the data
    data = cursor.fetchone()

    # Load data into a DataFrame and print
    df_min_max = pd.DataFrame([data], columns=['Minimum Assets', 'Maximum Assets'])
    print("\nMinimum and Maximum Managed Assets:")
    print(df_min_max)

except mysql.connector.Error as err:
    if err.errno == errors.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username or password.")
    elif err.errno == errors.ER_BAD_DB_ERROR:
        print("Error: Database does not exist.")
    else:
        print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()