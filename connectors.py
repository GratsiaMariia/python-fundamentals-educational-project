import mysql.connector
from mysql.connector import Error
from configs import DB_CONFIG_QUERY
from configs import DB_CONFIG_WRITE

def create_connection_mysql_db_query():
    try:
        connection_query = mysql.connector.connect(**DB_CONFIG_QUERY)
        print(f"Connection to Database {DB_CONFIG_QUERY['database']} successful")
        return connection_query
    except Error as e:
        print(f'Error connecting to MySQL Platform: {e}')
        return None

def create_connection_mysql_db_write():
    try:
        connection_write = mysql.connector.connect(**DB_CONFIG_WRITE)
        print(f"Connection to Database {DB_CONFIG_WRITE['database']} successful")
        return connection_write
    except Error as e:
        print(f'Error connecting to MySQL Platform: {e}')
        return None
