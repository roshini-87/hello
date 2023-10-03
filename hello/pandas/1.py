import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Roshini@8752",
    database="roshini"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute SQL queries here
cursor.execute("SELECT * FROM a")

# Fetch the results
results = cursor.fetchall()

# Do something with the results

# Close the cursor and connection
cursor.close()
conn.close()