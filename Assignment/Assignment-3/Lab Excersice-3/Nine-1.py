import sqlite3

con = sqlite3.connect("first.db")

# q = "create table person(id int primary key, name varchar(20),age int(3))"
# q = "insert into person values(1,'Ankit',35)"
# q = "insert into person values(2,'Bhavik',30)"
# q = "insert into person values(3,'Kevin',25)"

# con.execute(q)
# con.commit()

q = "select * from person"

first = con.execute(q).fetchall()
for i in first:
    print(i)
