#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import os  # Import the 'os' module

# Retrieve database credentials from environment variables
DB_HOST = os.getenv('HBNB_MYSQL_HOST', 'localhost')  # Default to localhost
DB_USER = os.getenv('HBNB_MYSQL_USER')
DB_PASSWORD = os.getenv('HBNB_MYSQL_PWD')
DB_NAME = os.getenv('HBNB_MYSQL_DB')


if __name__ == '__main__':
    """Access to the database and get the states from the database."""

    # Create a connection to the database using environment variables
    db = MySQLdb.connect(host=DB_HOST, user=DB_USER,
                         passwd=DB_PASSWORD, db=DB_NAME)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SELECT query, sorting by id
    cur.execute("SELECT * FROM states ORDER BY id ASC") 

    # Fetch all rows
    states = cur.fetchall()  

    # Iterate and print the state tuples
    for state in states:
        print(state) 

    # Close the cursor and database connection
    cur.close() 
    db.close()
