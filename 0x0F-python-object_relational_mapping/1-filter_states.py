#!/usr/bin/python3
"""this to  lists all states start with N from hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username, mysql_password, database_name = sys.argv[1:]
    dbconn = MySQLdb.connect(host="localhost", user=mysql_username,
                             passwd=mysql_password, db=database_name)
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
