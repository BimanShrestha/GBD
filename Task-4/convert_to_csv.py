import json
import pandas as pd
# changing the max_columns value
pd.set_option('display.max_columns', 11)
#json.load() used to read the Json Document from the file
data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/1.json'))
#json_normalize a technique of organizing the data into multiple related tables, to minimize DATA REDUNDANCY.
df = pd.json_normalize(data["data"])
print(df)
len(df)
#DataFrame to a CSV File
df.to_csv("/home/biman/Desktop/ALL_TASK/Task-4/googleseo/csv/1.csv")
#Link,title,price,rating,reviewcount
