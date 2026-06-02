import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="db1"
)
# print("Connected")

cursor = con.cursor()
# cursor.execute("create database db1")
# cursor.execute("create table employee (id int primary key, name varchar(20), department varchar(20), salary int)")
# cursor.execute("insert into employee values (1,'Ankit','CSE',21000)")
# con.commit()
# print("Record insert successfully")

# q = "insert into employee values(%s,%s,%s,%s)"
# # v = (2,'Yash','IT',19000)
# v = (3,'Bhavik','Mech',18000)
# cursor.execute(q,v)
# con.commit()

# q = "insert into employee values(%s,%s,%s,%s)"
# data = [
#     (4,'Uday','Elec',17000),
#     (5,'Kenil','Civil',18000)
# ]
# cursor.executemany(q,data)
# con.commit()
# print("Inserted")

# q = "update employee set name=%s,department=%s,salary=%s where id=%s"
# v = ('Bhavik A','Mechanical',20000,3)
# cursor.execute(q,v)
# con.commit()

# q = "delete from employee where id=%s"
# v = (4,)
# cursor.execute(q,v)
# con.commit()

q = "select * from employee"
cursor.execute(q)
# data = cursor.fetchall()
data = cursor.fetchmany(2)
print(data)

