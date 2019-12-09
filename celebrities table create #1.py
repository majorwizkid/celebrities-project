import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
#create a table called "celebs" with 7 fields - id, name, last name, age....
sql = "create table celebs(celebID integer PRIMARY KEY, firstname text, lastname text, age text, email text, photo text, bio text)"
cursor.execute(sql)
#create a table called "members" with 6 fields - id, name, last name, age....
sql = "create table members(memberID integer PRIMARY KEY, firstname text, lastname text, age text, email text, bio text)"
cursor.execute(sql)
#commit the changes to the database
conn.commit()
conn.close()


