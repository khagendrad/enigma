import psycopg2
# creating connector 
def connector():
    return psycopg2.connect(
        host = 'localhost',
        database = 'broadway_db',
        user = 'postgres',
        password = 'postgres',
        port = 5432
    )