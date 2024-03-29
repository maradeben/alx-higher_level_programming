#!/usr/bin/python3
""" script to list all states from database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for i in cursor.fetchall():
        print(i)
    cursor.close()
    con.close()
