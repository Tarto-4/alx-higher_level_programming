#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    # Get database connection arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a SQL query to retrieve all states, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Iterate over the rows and print each state's information
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
