#!/usr/bin/env python3
#
import psycopg2  # module that connects to the database
# create a connection to the database
connection = psycopg2.connect(database="news")
# create a cursor object
cursor = connection.cursor()
# SQL query to be executed
query = "SELECT author FROM articles LIMIT 5"
cursor.execute(query)
# fetch the result of the query
results = cursor.fetchall()
for result in results:
    print(result)
connection.close()
