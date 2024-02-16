#!/usr/bin/python3
"""this to takes in an argument and displays all values in the states table
	from hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    dbconn = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    curs = dbconn.cursor()
    query = """
        SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC
    """
    query = query.format(argv[4])

    curs.execute(query)

    res = curs.fetchall()

    for line in res:
        print(line)
    curs.close()
    dbconn.close()
