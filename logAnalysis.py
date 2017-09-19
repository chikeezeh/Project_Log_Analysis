#!/usr/bin/env python3
#
import psycopg2  # module that connects to the database
# create a connection to the database
connection = psycopg2.connect(database="news")
# create a cursor object
cursor = connection.cursor()
# SQL querys to be executed
# The querys are put in a list
# so multiple querys can be executed by the python code.
query1 = "SELECT name FROM authors WHERE id =1"
query2 = "SELECT title FROM articles WHERE author = 1 LIMIT 1"
query3 = "SELECT status FROM log LIMIT 1"
querys = [query1, query2, query3]
results = []  # empty list to put the result for each query
for query in querys:
    #  execute each of the querys
    cursor.execute(query)
    # fetch the result of the query
    results.append(cursor.fetchall())

answers = ["Author with id = 1 is: ",
           "First article by Author 1 is: ", "The first status code is: "]
# use string format to print answers out.
print("\n{}{}\n".format(answers[0], results[0][0][0]))
print("{}{}\n".format(answers[1], results[1][0][0]))
print("{}{}\n".format(answers[2], results[2][0][0]))

connection.close()
