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
query1 = """SELECT articles.title, COUNT(log.path) as
            topArticle FROM log JOIN articles on
            log.path = CONCAT('/article/',articles.slug)
            GROUP BY articles.title ORDER BY topArticle DESC LIMIT 3"""

query2 = """SELECT authors.name, COUNT(log.path) as topAuthor
            FROM((log JOIN articles ON log.path =
            CONCAT('/article/',articles.slug))
            JOIN authors ON articles.author = authors.id)
            GROUP BY authors.name
            ORDER BY topAuthor DESC
            """
query3 = "SELECT dayDate,error FROM errorStatus WHERE error > 1"
querys = [query1, query2, query3]
results = []  # empty list to put the result for each query
for query in querys:
    #  execute each of the querys
    cursor.execute(query)
    # fetch the result of the query and add to the end of list results
    results.append(cursor.fetchall())


# a function that presents the result in a formated way.
def presentAns(result):
    for i in result:
        if len(result) >= 3:
            print('\n{} - {} views\n'.format(i[0], i[1]))
        else:
            print('{} - {}%\n'.format(i[0], round(i[1], 2)))


print('Top three articles by views\n' + '-' * 30)
presentAns(results[0])
print('Author rank by Article views\n' + '-' * 30)
presentAns(results[1])
print('Dates with more than 1% Error Rate\n' + '-' * 30)
presentAns(results[2])

connection.close()
