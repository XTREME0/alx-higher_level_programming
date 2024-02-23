#!/usr/bin/python3
""" print states from states using sqlalchemy """

if __name__ == "__main__":

    import sys
    from models_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    argv = sys.argv[1:]
    argc = len(argv)

    host = "localhost"
    port = 3306
    username = argv[0]
    password = argv[1]
    db_name = argv[2]
    name = argv[3]

    connection = f'mysql+mysqldb://{username}:{password}@{host}:{port}/{db_name}'
    crs = create_engine(connection)
    Base.metadata.create_all(crs)
    Session = sessionmake(bind=crs)
    s = session()
    f = s.query(State).first()
    if f is None:
        print("Nothing")
    else:
        print(f'{f.id}: {f.name}')
