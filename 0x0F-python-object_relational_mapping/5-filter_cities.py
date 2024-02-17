#!/usr/bin/python3
"""this to  lists all cities from hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
import sys

if __name__ == "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                             user=argv[1], passwd=argv[2], db=argv[3])
    curs = dbconn.cursor()
    curs.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """, (argv[4],))
    res = curs.fetchall()
    print(", ".join([row[1] for row in res]))
    curs.close()
    dbconn.close()
