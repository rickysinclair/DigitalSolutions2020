import sqlite3

# create name of database
database = 'Company.db'

# connect to database or create
conn = sqlite3.connect(database)

# loop condition
enter = input('Would you like to enter some values y/n: ')

while enter == 'y' or enter == 'Y':
    id_input = int(input('Enter your ID number: '))
    name_input = input('Enter your Name: ')
    dob_input = input('Enter your DOB yyyy-mm-dd: ')

    # enter values into table
    conn.execute("INSERT INTO Customers (Id,Name,Dob) VALUES ({0}, {1}, {2})".format(id_input, name_input, dob_input))

    # commit changes to db
    conn.commit()

    # loop condition
    enter = input('Would you like to enter some values y/n: ')

# commit changes to db
conn.commit()

# close connection
conn.close()
