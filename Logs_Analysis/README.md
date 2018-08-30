# Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree
 
# Project Overview:
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)


## Introduction
This is a python module that uses information of large database of a web server and draw business conclusions from that information. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The database includes three tables:
* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.


### Functions in log.py:
* **get_data():** Connects to the PostgreSQL database and returns a database connection.
* **popular_articles():** Prints most popular three articles of all time.
* **popular_authors():** Prints most popular article authors of all time.
* **days_with_error():** Print days on which more than 1% of requests lead to errors.
 

### Creating views:
creating view for question3("On which day did more than 1% of request lead to error?)

"""create view logs as
select to_char(time,'Mon dd,yyyy')as date,count(*) as logcount from log
group by date;"""

View "public.logs"
"""
  Column  |  Type  | Modifiers 
----------+--------+-----------
 date     | text   | 
 logcount | bigint | 
"""

"""create view errorlogs as 
Select to_char(time,'Mon dd,yyyy')as date,count(*) as errorcount from log
where status='404 NOT FOUND'
group by date;"""
 
View "public.errorlogs"
"""
Column   |  Type  | Modifiers 
------------+--------+-----------
 date       | text   | 
 errorcount | bigint | 
"""


###How to run this code:

1.Install the VM and Vagrant:
This project uses a virtual machine (VM) to run a SQL database server.

2.If you don't already have virtual box on your machine, you can download it here:
->https://www.virtualbox.org/wiki/DownloadOldBuilds51 
or for ubuntu type this command: sudo apt-get install virtual box

3.Download and install Vagrant (if you do not already have it installed). This is the software that configures the VM and allows the host (your machine) to talk to the VM:
-->https://www.vagrantup.com/
or for ubuntu type this commnad: 'sudo apt-get install vagrant'
->you should be able to run $ 'vagrant --version' after installation to see the version that was installed.

4.Download and unzip this file:https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip  This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

5.cd into this(FSND_Virtual_Machine) directory

6.cd into the vagrant/ subdirectory

7.Bring the VM up with the command 'vagrant up'

8.Log into the VM with 'vagrant ssh'

#Download the news data and run the commands to populate the database:
1.Download the news data from here:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

2.Unzip this file and move the newsdata.sql file into your vagrant directory

3.cd into the vagrant directory and run psql -d news -f newsdata.sql
-->This will connect to the news database and populate the tables with the data contained in the sql file.

#Download and run the log_analysis.py file
1.Clone this repository to your local drive: https://github.com/9snehal/Logs_Analysis

2.Copy the log_analysis.py file into the FSND_Virtual_Machine/vagrant directory.

3.Open a terminal window from the FSND_Virtual_Machine/vagrant directory, or simply open a terminal window and cd into that directory.

4Run vagrant ssh at the prompt to log in to the VM.
$ vagrant ssh

5.cd into the vagrant subdirectory
vagrant@vagrant:~$ cd /vagrant

6.Run the log_analysis.py program
vagrant@vagrant:/vagrant$ python log_analysis.py

7.The program's output will be displayed in the terminal window.


