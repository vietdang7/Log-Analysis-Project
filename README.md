# Log Analysis Project
The project is created for Udacity Full Stack Nanodegree Programme.

## Code Example
Here are some lines of example code:
1. log_analysis.py:
```
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

    except:
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


```

## Why I create this project?
This is one of projects of Full Stack Udacity Nanodegree. Main reason is to evaluate the skills I have learnt so far (Python and SQL).

## Getting Started
### Prerequisites
1. You need to have `Python3` 
2. Vagrant
3. VirtualBox
4. Code editor like **Atom** or **Sublime**

### Installation
1. Clone this project (Using `git`command: `git clone https://github.com/vietdang7/Log-Analysis-Project.git` or through your GitDesktop application)
2. Install VirtualBox
3. Install Vagrant

## Testing
1. Run Vagrant by type `vagrant up`, and `vagrant ssh`to log in
2. Download `news.sql` from Udacity Classroom's site and run command `psql -d news -f newsdata.sql`
3. Copy `log_analysis.py` to shared folder vagrant and run command `python3 log_analysis.py`from terminal on virtual machine

Results will be generated on terminal window.
An example of result can be seen from `Result_Out.txt`

## Views 
For questions 3, I use two views as below:
1. errors
```
CREATE VIEW erros AS
SELECT DATE(log.time) AS day,
CAST(COUNT(log.status) AS FLOAT) AS error_num 
FROM log
WHERE log.status = '404 NOT FOUND'
GROUP BY day;
```

2. total
```
CREATE VIEW total AS
SELECT DATE(log.time) AS day,
CAST(COUNT(log.status) AS FLOAT) AS total_num 
FROM log
GROUP BY day;
```

## Built With
- Python
- SQL

## Contribution
If you want to make contribution for this project, feel free to `fork` this project and make `pull request`

## License

- Copyright of news.sql is belong to [Udacity](https://github.com/udacity/).
- This project is licensed under the MIT license
