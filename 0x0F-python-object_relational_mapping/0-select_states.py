#!/usr/bin/python3
"""
This script connects to a MySQL database on localhost at port 3306 and lists all
states from the `hbtn_0e_0_usa` database, sorted in ascending order by `id`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, 
                         user=sys.argv[1], passwd=sys.argv[2], 
                         db=sys.argv[3])

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SELECT query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
