from executer_for_query import execute_query

def check_list_genres(connection_query):
    select_query = f"select distinct genres from movies;"
    results = execute_query(connection_query, select_query)
    genres = set()
    for result in results:
        for genre in result[0]:
            genres.add(genre)
    return ', '.join(genres)

def check_min_year(connection_query):
    select_query = f"select min(year) from movies;"
    result = execute_query(connection_query, select_query)
    if result:
        return result[0][0]
    return None

def check_max_year(connection_query):
    select_query = f"select max(year) from movies;"
    result = execute_query(connection_query, select_query)
    if result:
        return result[0][0]
    return None
