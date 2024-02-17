#!/usr/bin/python3
"""This takes in arguments and displays all values in the states table
   of hbtn_0e_0_usa where name matches the argument. But this time, safe from
   MySQL injections.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    conn.close()
