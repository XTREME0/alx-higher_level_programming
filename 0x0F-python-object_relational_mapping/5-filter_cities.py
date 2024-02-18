#!/usr/bin/python3
""" print states from states table and search based on first letter """

if __name__ == "__main__":

    import MySQLdb
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    host = "localhost"
    port = 3306
    username = argv[0]
    password = argv[1]
    db_name = argv[2]
    name = argv[3]

    connection = MySQLdb.connect(host=host, port=port,
                            user=username, password=password, database=db_name)
    crs = connection.cursor()
    crs.execute("SELECT cities.name FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id", name)
    r = crs.fetchall()
    for row in r:
        print(", ".join(row))
