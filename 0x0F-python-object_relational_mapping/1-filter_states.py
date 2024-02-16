#!/usr/bin/python3
"""this to  lists all states start with N from hbtn_0e_0_usa
"""
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
        SELECT *
        FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id
    """

    curs.execute(query)

    res = curs.fetchall()

    for line in res:
        print(line)
    curs.close()
    dbconn.close()
