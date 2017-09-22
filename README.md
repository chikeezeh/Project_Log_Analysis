# **OVERVIEW**

This project employs SQL and Python to query a database and answer 3 questions.
Which are:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## **QUICKSTART**

1. To run the program, install [Python 3](https://www.python.org/downloads/) and [PostgreSQL](https://www.postgresql.org/download/)
2. Download the [logAnalysis.py](https://github.com/chikeezeh/Project_Log_Analysis/blob/master/logAnalysis.py) file to a folder that contains the database file [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), you will need to unzip the database file.
3. The program requires the module psycopg2 to work so install that with ```pip install psycopg2```.
4. On your console use the command ```psql -d news -f newsdata.sql``` to create the database tables into your local database.
5. The SQL querys require 3 views to solve the problems, type the following codes in your console:

```SQL
CREATE VIEW statusTotal AS 
SELECT log.time::date AS dayDate,
CAST(COUNT(log.status) AS FLOAT) AS 
statusCount FROM log GROUP BY dayDate;
```

```SQL
CREATE VIEW statusOK AS 
SELECT log.time::timestamp::date AS dayDate, 
COUNT(log.status) AS statusCount FROM log 
WHERE log.status ='200 OK' GROUP BY dayDate;
```

```SQL
CREATE VIEW errorStatus AS 
SELECT statusTotal.dayDate,
(100*(1-(statusOK.statusCount/statusTotal.statusCount))) 
AS "error" FROM statusTotal JOIN statusOK 
ON statusTotal.dayDate = statusOK.dayDate;
```

6. Type ```python3 logAnalysis.py``` on your console to run the program.

## **HOW THE PROGRAM WORKS**
1. To answer the first question, table *articles* and *log* are joined. The slug column in table articles is concatenated with */article/* to match it with the content of column path on table log. log.path is counted and grouped by articles.slug and the results are sorted in descending order.

2. To answer question 2, A 3 table join is performed here to get a table with the authors name and their artcle view count.

3. Question 3 employs the 3 views created as shown above, and the date with error greater than 1% is selected. 

## **LICENSE**
MIT License

Copyright (c) [2017] [Chike Ezeh]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
