# Import Python DB API for PSQL
import psycopg2

# Set database name
DBNAME = 'news'

# Create function to connect to database
def connectDatabase(query):
    """
    This function setup connect to database in DBNAME then execute the 'query',
    return the result in 'result'
    """
    try:
        database = psycopg2.connect('dbname=' + DBNAME)
        cursor = database.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
        database.close()

    except :
        print("Can not connect to the database")

# Create function question_one
def question_one():
    """
    This function will return the result for question 1:
    What are the most popular three articles of all time?
    """
    query_one = """SELECT articles.title, COUNT(log.id) AS views
    FROM log, articles
    WHERE log.path = CONCAT('/article/', articles.slug)
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3;"""
    result_one = connectDatabase(query_one)
    print('1.What are the most popular three articles of all time?')
    for result in result_one:
        print('"' + result[0] + '" -- ' + str(result[1]) + " views")
    print('\n')

# Create function question_two
def question_two():
    """
    This function will return the result for question 2:
    Who are the most popular article authors of all time?
    """
    query_two = """ SELECT authors.name, COUNT(log.id) AS views
    FROM authors, articles, log
    WHERE authors.id = articles.author AND
    log.path = CONCAT('/article/', articles.slug)
    GROUP BY authors.name
    ORDER BY views DESC;
    """
    result_two = connectDatabase(query_two)
    print('2. Who are the most popular article authors of all time?')
    for result in result_two:
        print('"' + result[0] + '" -- ' + str(result[1]) + " views")
    print('\n')

# Create function question_three
def question_three():
    """
    This function will return the result for question 3:
    On which days did more than 1% of requests lead to errors?
    """
    query_three = """
    SELECT total.day AS day, ((errors.error_num/total.total_num)*100) AS percentage
    FROM total, errors
    WHERE ((errors.error_num/total.total_num)*100) > 1
    AND total.day = errors.day
    ORDER BY day;
    """
    result_three = connectDatabase(query_three)
    print('3. On which days did more than 1% of requests lead to errors?')
    for result in result_three:
        print (result[0], "--", str(result[1]) + "% errors")
    print('\n')

question_one()
question_two()
question_three()
