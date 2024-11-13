# C:\Users\ICH>python C:\Users\ICH\IdeaProjects\MyProject\work.py

import mysql
import mysql.connector
from mysql.connector import connect
from mysql.connector import Error

def create_connection_mysql_db_query():
    dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
                'user': 'ich1',
                'password': 'password',
                'database': 'movies'}

    try:
        connection = mysql.connector.connect(**dbconfig)
        print(f"Connection to Datebase {dbconfig['database']} successful")
        return connection
    except Error as e:
        print(f'Error connecting to MySQL Platform: {e}')
        return None

create_connection_mysql_db_query()

def create_connection_mysql_db_write():
    dbconfig_write = {
        'host': 'mysql.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'database': '271123dam_Mariia'}

    try:
        connection1 = mysql.connector.connect(**dbconfig_write)
        print(f"Connection to MySQL {dbconfig_write['database']} successful")
        return connection1
    except Error as e:
        print(f'Error connecting to MySQL Platform: {e}')
        return None

create_connection_mysql_db_write()

def execute_query(connection, query, parameters=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, parameters if parameters is not None else ())
        if query.strip().lower().startswith("select"):
            return cursor.fetchall()
        else:
            connection.commit()
    except Error as e:
        print(f'An error occurred: {e}')
        connection.rollback()
        return None
    finally:
        cursor.close()

def insert_in_table_db(connection1, text_query, query_type, keyword):
    insert_query = f"INSERT INTO `History` (`Text_query`, `Query_type`, `Keyword`) VALUES (%s, %s, %s);"
    execute_query(connection1, insert_query, (text_query, query_type, keyword))

def check_keywords(connection, connection1, keyword):
    select_query = f"SELECT title, plot, year FROM movies WHERE plot like '%{keyword}%';"
    results = execute_query(connection, select_query)
    for result in results:
        print(result)
    insert_in_table_db(connection1, select_query, "keywords_in_plot", keyword)

def check_genres_years(connection, connection1, genre, year):
    select_query = f"SELECT title, genres, year FROM movies WHERE genres like '%{genre}%' and year = {year};"
    results = execute_query(connection, select_query)
    for result in results:
        print(result)
    insert_in_table_db(connection1, select_query, "genre and year", f"Genre: {genre}, Year: {year}")

def check_rating_years(connection, connection1, year):
    select_query = f"SELECT title, year, `imdb.rating` FROM movies WHERE year = {year} AND `imdb.rating` = (SELECT MAX(`imdb.rating`) AS max_rating FROM movies where year = {year});"
    results = execute_query(connection, select_query)
    for result in results:
        print(result)
    insert_in_table_db(connection1, select_query, "rating and year", year)

def check_history(connection1):
    select_query = f"SELECT Query_type, Text_Query, Keyword, COUNT(*) OVER (PARTITION BY Query_type) AS cnt_query FROM History ORDER BY cnt_query DESC;"
    results = execute_query(connection1, select_query)
    for result in results:
        print(result)

def main():
    connection = create_connection_mysql_db_query()
    connection1 = create_connection_mysql_db_write()

    print("Let's look for movies in the movies database. You can select films by keyword in the description, by genre and year, by rating and year, and also view the most popular queries.")

    while True:
        number_query = int(input('To search, enter: 1 - keyword, 2 - genres and year, 3 - rating and year, 4 - query history, 0 - end search: '))
        if number_query == 1:
            keyword = input('Insert keywords for query in plot: ')
            check_keywords(connection, connection1, keyword)
        elif number_query == 2:
            genre = input('Insert genre for query: ')
            year = int(input('Insert year for query in genres: '))
            check_genres_years(connection, connection1, genre, year)
        elif number_query == 3:
            year = int(input('Insert year for query in rating: '))
            check_rating_years(connection, connection1, year)
        elif number_query == 4:
            check_history(connection1)
        elif number_query == 0:
            break
        else:
            print(f'Invalid input. Try again {number_query}')

    connection.close()
    connection1.close()

if __name__ == "__main__":
    main()
