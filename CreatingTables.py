import mysql.connector

#-----------Establishing the connection between python and mysql--------------
conn=mysql.connector.connect(host='localhost',user='root',passwd='1234')
if conn.is_connected():
    print('connected succesfully')

#-----------------------Creating the database ‘library’--------------------------------
cur = conn.cursor()
cur.execute('create database library')

#--------------------------Creating table ‘books table’---------------------------------
sql= conn.cursor()
sql.execute('create table book(title varchar(20),author varchar(30),price integer,pages integer,publisher varchar(30),edition integer,status varchar(15))')

#--------------------------Creating table ‘members table’-----------------------------
sql= conn.cursor()
sql.execute('create table member(name varchar(30) ,class varchar(10),address varchar(50),phone integer,email varchar(30) )')
