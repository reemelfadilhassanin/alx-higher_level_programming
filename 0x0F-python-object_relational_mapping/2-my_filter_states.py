#!/usr/bin/python3
"""this to takes in an argument and displays all values in the states table
	from hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    dbconn = MySQLdb.connect(user=argv[1], port=3306, host="localhost",
                             passwd=argv[2], db=argv[3])

    curs = dbconn.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))

    res = curs.fetchall()
    for row in res:
        if row[1] == argv[4]:
            print(row)
    curs.close()
    dbconn.close()
