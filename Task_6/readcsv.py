import pandas as pd
import psycopg2
from pandas import DataFrame

# import csv
data =pd.read_csv(r'/home/biman/Desktop/ALL_TASK/Task_6/1.csv')
df=pd.DataFrame(data)
print(df)


# connect to sql server
con=psycopg2.connect(
    host="localhost",
    database="gbd",
    user="postgres",
    password="1999",
    port="5432",
)
cursor=con.cursor()

# Creating a Table
cursor.execute(''''SELECT *
# FROM Employee
# ORDER BY salary ASC;''')


