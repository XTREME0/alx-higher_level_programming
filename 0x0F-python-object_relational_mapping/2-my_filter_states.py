#!/usr/bin/python3
""" print states from states table and search based on first letter """

if __name__ == "__main__":

    import MySQLdb
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    host = "localhost"
    port = 3306
    if argc < 4:
        exit()
    username = argv[0]
    password = argv[1]
    db_name = argv[2]
    search = argv[3]

    connection = MySQLdb.connect(host=host, port=port,
                            user=username, password=password, database=db_name)
    crs = connection.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY 'id';".format(search))
    r = crs.fetchall()
    for row in r:
        print(row)
