#!/usr/bin/python3
"""this to lists all states with a name starting with N (upper N)from hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
    curs = dbconn.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    find = curs.fetchall()
    for line in find:
        print(line)
    curs.close()
    dbconn.close()
