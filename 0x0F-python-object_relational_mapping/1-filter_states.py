#!/usr/bin/python3
"""
This script connects to a MySQL database on localhost at port 3306 and lists
all states whose names start with 'N' from the `hbtn_0e_0_usa` database,
sorted in ascending order by `id`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost", 
        port=3306, 
        user=sys.argv[1], 
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SELECT query with a WHERE clause to filter by name
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
