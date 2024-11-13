**Movie Search Console Application - Python Educational Project**
This project is a Python console application for searching movies in the Sakila database. The application allows users to search movies, save all search keywords in a separate table, and display the most popular searches based on user queries. This README provides a summary of the completed steps and key features of the project.

**Project Summary**
The application connects to the Sakila movie database, which is installed on a local server. Users can perform movie searches, and each search is stored in a log table to track popular search terms.

**Completed Tasks**
Database Connection and Table Exploration

**Successfully connected to the Sakila database on a local database server.**
Explored the structure of the tables in Sakila, identified the relationships, and noted data types to understand the database’s setup.
Tested a few SQL queries to retrieve specific movies, such as movies of a certain genre or released in a specific year, to confirm the database schema and relationships.

**SQL Query Development for Movie Searches**
Developed and tested SQL queries that retrieve movies based on search criteria provided by the user.
Queries are optimized to handle searches for specific genres, release years, and other movie-related filters.
These SQL queries are now integrated into the Python application, enabling live search functionality.

**Saving Search Keywords**
Created an additional table to store all search keywords used by the user in the application.
Implemented SQL queries within the Python application to insert each new search term into this table immediately after a search is performed.
This logging table now stores all search history, allowing for detailed analysis of search terms.

**Displaying Popular Search Terms**
Developed and tested SQL queries that rank search keywords by frequency.
Added a feature in the Python application that lets users view the most popular search terms in descending order.
Popular search terms are displayed based on their frequency, giving users insight into common search interests.

**Key Features**
**Movie Search:** Real-time movie search using SQL queries with filters for genre and release year.
**Search Term Logging:** Automatic logging of every search term in a dedicated table.
**Popularity Ranking:** A feature to display the most frequently searched terms, ranked by popularity.

**Additional Information**
**Modules:** The project is organized into modules for database connection, search, logging, and popularity ranking.
