#!/usr/bin/python3
""" script to list all cities from given state in hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], password=argv[2], database=argv[3],
        charset='utf8')
    cursor = con.cursor()
    cursor.execute("""
        SELECT c.name
        FROM cities AS c
        JOIN states as s
        ON c.state_id=s.id
        WHERE s.name=%s
        ORDER BY c.id ASC
        """, (argv[4],))

    print(", ".join([city[0] for city in cursor.fetchall()]))
    cursor.close()
    con.close()
