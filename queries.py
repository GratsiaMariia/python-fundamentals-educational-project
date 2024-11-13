from executer_for_query import execute_query
from tips import check_list_genres
from tips import check_min_year
from tips import check_max_year
from print_results import print_results_as_table

def insert_in_table_db(connection_write, text_query, query_type, keyword):
    insert_query = f"INSERT INTO `History` (`Text_query`, `Query_type`, `Keyword`) VALUES (%s, %s, %s);"
    execute_query(connection_write, insert_query, (text_query, query_type, keyword))

def check_keywords(connection_query, connection_write, keyword):
    select_query = f"SELECT title, plot, year FROM movies WHERE plot like '%{keyword}%' limit 10;"
    results = execute_query(connection_query, select_query)
    if not results:
        print("No results found for the keyword.")
    else:
        print_results_as_table(results, ["Title", "Plot", "Year"])
        insert_in_table_db(connection_write, select_query, "keywords_in_plot", keyword)

def check_genres_years(connection_query, connection_write, genre, year):
    select_query = f"SELECT title, genres, year FROM movies WHERE genres like '%{genre}%' and year = {year} limit 10;"
    results = execute_query(connection_query, select_query)
    if not results:
        genre_list = check_list_genres(connection_query)
        min_year = check_min_year(connection_query)
        max_year = check_max_year(connection_query)
        print(f"No results found for the genre and year. \nChoose period between {min_year} and {max_year} \nand genres from: {genre_list}")
    else:
        print_results_as_table(results, ["Title", "Genres", "Year"])
        insert_in_table_db(connection_write, select_query, "genre and year", f"Genre: {genre}, Year: {year}")

def check_rating_years(connection_query, connection_write, year):
    select_query = f"SELECT title, year, `imdb.rating` FROM movies WHERE year = {year} AND `imdb.rating` = (SELECT MAX(`imdb.rating`) AS max_rating FROM movies where year = {year});"
    results = execute_query(connection_query, select_query)
    min_year = check_min_year(connection_query)
    max_year = check_max_year(connection_query)
    if not results:
        print(f"No results found for the rating in YEAR. \nChoose period between {min_year} and {max_year}")
    else:
        print_results_as_table(results, ["Title", "Year", "Rating"])
        insert_in_table_db(connection_write, select_query, "rating and year", year)

def check_history(connection_write):
    while True:
        choice_history = input("Select FULL for extended information and SHORT for short information: ").strip().lower()
        if choice_history == "full":
            select_query = ("SELECT Query_type, Text_Query, Keyword, COUNT(*) OVER (PARTITION BY Query_type) AS cnt_query FROM History ORDER BY cnt_query DESC;")
            columns = ["Query_type", "Text_Query", "Keyword", "CNT_query"]
        elif choice_history == "short":
            select_query = ("SELECT Query_type, COUNT(*) AS cnt_query FROM History GROUP BY Query_type ORDER BY cnt_query DESC;")
            columns = ["Query_type", "CNT_query"]
        else:
            print("Invalid input. Please enter 'full' or 'short'.")
            continue
        results = execute_query(connection_write, select_query)
        print_results_as_table(results, columns)
        break

def check_directors_query_with_star(connection_query, connection_write, director):
    select_query = f"select title, directors from movies where JSON_CONTAINS(directors, '\"{director}\"') limit 10;"
    results = execute_query(connection_query, select_query)
    if not results:
        print("No results found for the keyword.")
    else:
        print_results_as_table(results, ["Title", "Director"])
        insert_in_table_db(connection_write, select_query, "directors_query", director)