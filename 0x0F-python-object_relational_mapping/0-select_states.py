#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    argv = sys.argv[1:]
    argc = len(argv)

    host = "localhost"
    port = 3306
    if argc < 3:
        exit()
    username = argv[0]
    password = argv[1]
    db_name = argv[2]

    connection = MySQLdb.connect(host=host, port=port, user=username, password=password, database=db_name)
    crs = connection.cursor()
    crs.execute("SELECT * FROM states ORDER BY 'id';")
    r = crs.fetchall()
    for row in r:
        print(row)
    crs.close()
    connection.close()
