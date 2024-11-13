
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