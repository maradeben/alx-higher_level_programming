#!/usr/bin/python3
""" script to list all states matching user input
    from database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("""
        SELECT c.id, c.name, s.name
        FROM cities AS c
        JOIN states AS s
        ON c.state_id = s.id
        ORDER BY c.id ASC""")

    for result in cursor.fetchall():
        print(result)
    cursor.close()
    con.close()
