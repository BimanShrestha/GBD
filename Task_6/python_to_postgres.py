import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database = "gbd",
    user = 'postgres',
    password = '1999',
    port = '5432'
)
# print(conn)
cur = conn.cursor()
# cur.execute("""CREATE TABLE Employees(
#     id INT PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     DepartmentId VARCHAR (100) NOT null,
#     Salary INT,
#     Active INT
# );
# """)

# cur.execute("""CREATE TABLE Departments(
#     id INT PRIMARY KEY,
#     name VARCHAR(50) NOT NULL
# );""")

# cur.execute('''INSERT INTO Departments(id, name)
# VALUES
#     (1, 'IT'),
#     (2, 'Admin'),
#     (3, 'HR'),
#     (4, 'Accounts'),
#     (5, 'Health');''')

# cur.execute('select * from  Departments')
# cur.execute('''INSERT INTO Employees(id, name,DepartmentId,Salary,Active)
# VALUES
#     (1, 'John','IT',2000,1),
#     (2, 'Sean','IT',4000,1),
#     (3, 'Eric','Admin',2000,1),
#     (4, 'Nancy','Admin',2000,1),
#     (5, 'Lee','HR',3000,1),
#     (6, 'Steven','Accounts',2000,1),
#     (7, 'Matt','IT',5000,1),
#     (8, 'Sarah','IT',2000,0);''')
# data=cur.fetchall()
# # cur.execute('select * from  Employees')
# # data=cur.fetchall()
# print(data)
#
# cur.execute('''SELECT *
# FROM Employee
# ORDER BY salary ASC;''')
# data=cur.fetchall()
# print(data)
# data_df=pd.DataFrame(data,columns=('id','name','departmentid','Salary','active'))
# data_df.to_csv("1.csv",index=False)
# cur.execute('Select * from Employee ORDER BY salary desc  limit 2;')
# data=cur.fetchall()
# print(data)
# data_df=pd.DataFrame(data,columns=('id','name','departmentid','Salary','active'))
# data_df.to_csv("6.csv",index=False)
cur.execute('select e."name" , d."name"  from employee e join department d on e.departmentid = d."name" ;')
data=cur.fetchall()
print(data)
data_df=pd.DataFrame(data,columns=('name','departmentid'))
data_df.to_csv("7.csv",index=False)
conn.commit()
cur.close()
conn.close()