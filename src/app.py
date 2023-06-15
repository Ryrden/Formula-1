# Create a connection with a database which already exists
# The information to log on database are

'''
- **Host:** localhost
- **Port:** 5432
- **login:** postgres
- **password:** postgres
- **database:** postgres
- **url:** jdbc:postgresql://localhost:5432/postgres
'''

# Importing the libraries
import psycopg2

# Create a connection with a database
connection = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="postgres",
    database="postgres"
)

# Create a cursor
cursor = connection.cursor()

# Select all data from a table
cursor.execute("SELECT * FROM airports")