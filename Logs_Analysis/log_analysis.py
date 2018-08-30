#Log Analysis project
# import PostgreSQL library
import psycopg2
DBNAME="news"
def get_data(query):
    """fetch data from database"""
    db=psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c.execute(query)
    data=c.fetchall()
    db.close()
    return data

# 1.What are the most popular three articles of all time?
def popular_articles():
    """display the three popular articles"""
    query="Select articles.title,count(*) as total_views from articles,log  where log.path like concat('/article/',articles.slug) group by articles.title order by total_views desc limit 3"
    result=get_data(query)
    print(" 1. The most popular three articles of all time:")
    print("")
    for record in result:
        print('   ' + '\"' + str(record[0]) + '\"' + '-' + ' ' + str(record[1]) + ' '+ 'views')
        print(" ")

# 2.Who are the most popular articles author of all time?
def popular_authors():
    """display the popular authors"""
    query="Select authors.name,count(*) as total_views from authors,articles,log where log.path like concat ('/article/',articles.slug) and articles.author=authors.id group by authors.name order by total_views desc"
    result=get_data(query)
    print(" 2. The most popular articles authors of all time:")
    print("")
    for record in result:
        print('   ' +' ' + str(record[0]) + ' -' + ' ' + str(record[1]) + ' ' +'views')
        print(" ")

# 3.On which days did more than 1% of request lead to errors?
# create views for question 3 as instructed on README.md file
def days_with_error():
    """display the days with error more than 1%"""
    query="Select errorlogs.date,round(100.0*errorcount/logcount,2) as Percent from logs,errorlogs where logs.date=errorlogs.date and errorcount>logcount/100"
    result=get_data(query)
    print(" 3. Days with more than 1% of error:")
    print("")
    for record in result:
        print('   ' + str(record[0]) + ' '+ '-' + " " + str(record[1]) + '%'+ ' '+ 'errors')
        print("\t")

  #print results
popular_articles()
print(" ")
popular_authors()
print(" ")
days_with_error()
