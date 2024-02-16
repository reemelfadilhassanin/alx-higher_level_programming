#!/usr/bin/python3
"""Script that displays all values in the states table of hbtn_0e_0_usa
   where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)

    curs = dbconn.cursor()

    curs.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    res = curs.fetchall()

    for line in res:
        print(line)
    curs.close()
    dbconn.close()
