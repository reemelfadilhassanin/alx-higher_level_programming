#!/usr/bin/python3
"""this to  lists all cities from hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
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
		SELECT cities.name FROM cities JOIN states ON 
		cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC
	"""

    curs.execute(query)
    print(", ".join([city[2] for city in curs.fetchall()
                     if city[4] == argv[4]]))
    curs.close()
    dbconn.close()
