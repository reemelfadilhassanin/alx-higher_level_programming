#!/usr/bin/python3
"""this to takes in an argument and displays all values in the states table
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                             user=argv[1], passwd=argv[2], db=argv[3])
    curs = dbconn.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    curs.execute(q)
    res = curs.fetchall()
    for row in res:
        print(row)
    curs.close()
    dbconn.close()
