# Question 1
"""A database is an organised collection of structured information or data typically stored electronically 
in a computer system. a database is usually controlled by database management system (DBMS).

# 5 difference between sql and nosql databases
1. sql database are relational and nosql databases are non relational.
2. sql databases are structured query language (sql) and have a predefined schema. Nosql databases have 
dynamic schemas for unstructured data.
3. SQL databases are vertically scalable while Nosql databases are horizontally scalable.
4. SQL databases are table based while Nosql databases are document , keyvalue ,graph or 
wide column stores.
5. Sql databases are better for multirow transactions while Nosql is better for unstructured data like
documents or json."""



 # Question 2 
"""Data Definition Language (DDL) describes the portion of sql that create ,alter, and delete database objects.

 Create - Create is used to create a table or database in sql.  syntax -  CREATE TABLE Table name(columns...) ;

 DROP - The drop table command deletes a table in the database. synatx - DROP TABLE table name;

 ALTER - The alter table command adds , deletes and modifies columns in a table. 
 synatx - ALTER TABLE table name  ADD column name ;  # add or delete or modify.

TRUNCATE - The truncate table command deletes the data inside a table but not the table itself.
syntax - TRUNCATE TABLE table name ;"""


# Question 3
"""The SQL commands that deals with the manipulation of data present in the database belong to DML or Data 
Manipulation Language and this includes most of the sql statements. 

INSERT - It is used to insert data into a table.  
syntax - INSERT INTO table name VALUES (given values ...)

UPDATE - It is used to update existing data within a table.  
syntax - UPDATE table name SET (column and values) Where (criteria is met)

DELETE - It is used to delete records from a database table. 
syntax - DELETE FROM table name WHERE (criteria is met)"""



# Question 4
"""DQL is a portion of a SQL statement that allows you to get and organise data from a database.
The select command allows getting the data out of the database to perform operations with it.

SELECT - It is used to retrive data from the database. 
syntax - SELECT column name FROM table name"""



# Question 5
"""Primary Key - A primary key is used to insure that data in the specific column is unique. a column can 
not have null values. it is either an existing table column or a column that is specifically generated 
by the database according to a defined sequence.

Foreign Key - A foreign key is a column or group of columns in a relational database table that 
provides a link between data in two tables. it is a column or columns that references a column 
(most often the primary key) of another table."""



# Question 6
import mysql.connector

mywork = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
mycursor =  mywork.cursor()  
# cursor is created by the connection it is an object which helps to execute the query and fetch 
# the records from the database.
mycursor.execute("create database work")
# Allows python code to execute mysql command in a database session.



# Question 7
"""The order of execution of SQL clauses in an SQL query are -
1. FROM
2. ON 
3. JOIN
4. wHERE 
5. GROUP BY 
6. HAVING 
7. SELECT 
8. ORDER BY 
9. LIMIT """
