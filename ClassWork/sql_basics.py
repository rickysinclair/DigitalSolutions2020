import sqlite3

names = []
life = []

# create name of database
database = 'world.db'

# create connection to the database
conn = sqlite3.connect(database)

# query database
record = conn.execute('SELECT Name, Lifeexpectancy FROM Country '
                      'WHERE Lifeexpectancy > 75 AND Population < 1000000 ORDER BY Lifeexpectancy DESC ')

# print records
for row in record:
    names.append(row[0])
    life.append(row[1])

print(names)
print(life)
# close connection
conn.close()