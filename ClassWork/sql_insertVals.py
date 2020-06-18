import sqlite3

# create name of database
database = 'Company.db'

# connect to database or create
conn = sqlite3.connect(database)

# drop table if database already exists
conn.execute("DROP TABLE IF EXISTS Customers;")

# create table with primary key, fields and datatypes
conn.execute('''CREATE TABLE Customers
            (Id TEXT PRIMARY KEY NOT NULL,
             Name TEXT NOT NULL,
             Dob DATE NOT NULL);''')

# enter values into table
conn.execute("INSERT INTO Customers (Id,Name,Dob) VALUES (1234,'Fisher','2018-01-11');")
conn.execute("INSERT INTO Customers (Id,Name,Dob) VALUES (1345,'Palmer','2010-03-03');")
conn.execute("INSERT INTO Customers (Id,Name,Dob) VALUES (1456,'Olufson','2016-07-12');")

# commit changes to db
conn.commit()

# close connection
conn.close()

