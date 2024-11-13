import re
from connectors import create_connection_mysql_db_query, create_connection_mysql_db_write
from queries import check_keywords, check_genres_years, check_rating_years, check_history, check_directors_query_with_star
from mistakes import continue_or_exit

def main():
    connection_query = create_connection_mysql_db_query()
    connection_write = create_connection_mysql_db_write()

    print(f"\n Let's look for movies in the movies database. You can select films: \n by keyword in the description,\n by genre and year,\n by rating and year,\n by director,\n and also view the most popular queries.")

    try:
        while True:
            number_query = input(f'\n To search, enter: KEYWORD - 1, GENRES and YEAR - 2, Rating in YEAR - 3, QUERY HISTORY - 4, DIRECTOR -5, EXIT - 0: ')
            if number_query.isdigit():
                number_query = int(number_query)
            else:
                print("Please enter a valid NUMBER.")
                continue

            if number_query == 1:
                while True:
                    keyword = input(f'\nInsert KEYWORD for query in plot: ')
                    if keyword.strip() and re.match("^[A-Za-z0-9 -]+$", keyword):
                        check_keywords(connection_query, connection_write, keyword)
                        break
                    if not continue_or_exit("KEYWORD cannot be empty"):
                        break

            elif number_query == 2:
                while True:
                    genre = input(f'\n Insert GENRE for query: ')
                    if genre.strip() and re.match("^[A-Za-z -]+$", genre):
                        while True:
                            year = input(f'\nInsert YEAR for query in genres: ')
                            if year.isdigit():
                                year = int(year)
                                check_genres_years(connection_query, connection_write, genre, year)
                                break
                            if not continue_or_exit("Please enter a valid YEAR"):
                                break
                        break
                    if not continue_or_exit("GENRE must be in English letters only"):
                        break

            elif number_query == 3:
                while True:
                    year = input(f'\n Insert YEAR for query in rating: ')
                    if year.isdigit():
                        year = int(year)
                        check_rating_years(connection_query, connection_write, year)
                        break
                    if not continue_or_exit("Please enter a valid YEAR"):
                        break
                    break

            elif number_query == 4:
                check_history(connection_write)


            elif number_query == 5:
                while True:
                    director = input(f'\nInsert DIRECTOR for query: ')
                    if director.strip() and re.match("^[A-Za-z0-9 -]+$", director):
                        check_directors_query_with_star(connection_query, connection_write, director)
                        break
                    if not continue_or_exit("DIRECTOR cannot be empty"):
                        break

            elif number_query == 0:
                print(f'\n Danke für Ihre Aufmerksamkeit. Chao')
                break
            else:
                print(f'Invalid input. Try again {number_query}')

    finally:
        connection_query.close()
        connection_write.close()

if __name__ == "__main__":
    main()
