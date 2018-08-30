#!/usr/bin/env python
#Log Analysis project
# import PostgreSQL library
import psycopg2
DBNAME= "news"


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
    query="SELECT articles.title,count(*) AS total_views FROM articles,log  WHERE log.path like concat('/article/',articles.slug) group by articles.title order by total_views desc limit 3"
    result=get_data(query)
    print(" 1. The most popular three articles of all time:")
    print("")
    for record in result:
        print('   ' + '\"' + str(record[0]) + '\"' + '-' + ' ' + str(record[1]) + ' '+ 'views')
        print(" ")


# 2.Who are the most popular articles author of all time?
def popular_authors():
    """display the popular authors"""
    query="SELECT authors.name,count(*) AS total_views FROM authors,articles,log WHERE log.path like concat ('/article/',articles.slug) AND articles.author=authors.id group by authors.name order by total_views desc"
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
    query="SELECT errorlogs.date,round(100.0*errorcount/logcount,2) As Percent FROM logs,errorlogs WHERE logs.date=errorlogs.date AND errorcount>logcount/100"
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
