import mysql.connector

# Establish the connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ankit@7677",
    database="movie"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Example query
cursor.execute("SHOW TABLES")

# Fetch and print the results
for table in cursor:
    print(table)

# Close the connection
cursor.close()
connection.close()