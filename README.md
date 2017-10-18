# Log Analysis Project
The project is created for Udacity Full Stack Nanodegree Programme.

## Code Example
Here are some lines of example code:
1. log_analysis.py:
```python
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
Database used in this project is a PostgreSQL database (named `news`) for a fictional news website.

## Project's question
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Structure of the database 


## Getting Started
### Prerequisites
1. You need to have `Python3` 
2. [Vagrant](https://www.vagrantup.com/downloads.html)
3. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

### Installation
1. Clone this project (Using `git`command: `git clone https://github.com/vietdang7/Log-Analysis-Project.git` or through your GitDesktop application)
2. Install VirtualBox
3. Install Vagrant
4. Download this [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) from Udacity (this will install all needed OS, software in your VirtualBox)
5. Unzip the file, change to this directory in your terminal - `cd` command.
6. Run Vagrant by type `vagrant up`, and `vagrant ssh`to log in


## Testing
1. Download [`newsdata.zip`](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from Udacity Classroom's site and run command `psql -d news -f newsdata.sql`
2. Create views with this command `psql -d news -f create_views.sql` (`create_views.sql`should be inside Vagrant folder)
3. Copy `log_analysis.py` to shared folder vagrant and run command `python3 log_analysis.py`from terminal on virtual machine

Results will be generated on terminal window.
An example of result can be seen from `Result_Output.txt`

## Views 
For questions 3, I use two views as below:
1. errors
```sql
CREATE VIEW errors AS
SELECT DATE(log.time) AS day,
CAST(COUNT(log.status) AS FLOAT) AS error_num 
FROM log
WHERE log.status = '404 NOT FOUND'
GROUP BY day;
```

2. total
```sql
CREATE VIEW total AS
SELECT DATE(log.time) AS day,
CAST(COUNT(log.status) AS FLOAT) AS total_num 
FROM log
GROUP BY day;
```

## Built With
- Python3
- SQL

## Contribution
If you want to make contribution for this project, feel free to `fork` this project and make `pull request`

## License

- Copyright of `news.sql`, FSND-Virtual-Machine.zip  is belong to [Udacity](https://github.com/udacity/).
- This project is licensed under the MIT license
