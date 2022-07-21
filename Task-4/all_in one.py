import os, json
import pandas as pd

data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/71.json'))
df = pd.json_normalize(data["data"])
df = pd.DataFrame(df)
final_series = pd.DataFrame()
df = pd.json_normalize(data["data"])
df = pd.DataFrame(df)
#Air Filter Suppliers location
df2 = df[df['element'].str.contains('SPAN') & (df['x']==28)& (df['height']==24)]
print(df2)
df2.to_csv('shopname.csv')
df3= df[df['element'].str.contains('SPAN') & (df['x']==51.46875)& (df['height']==11.390625)&df['attributes.role'].str.contains('img')]
print(df3)
df3.to_csv('shoprating.csv')
df4 = df[df['element'].str.contains('SPAN')& (df['depth']==24)&df['attributes.role'].str.contains('text')]
print(df4)
df4.to_csv('shopreviewcount.csv')
df5 = df[df['element'].str.contains('SPAN')& (df['depth']==23)&(df['height']==16)]
print(df5)
df5.to_csv('shopopening closing.csv')
df17 = df[df['parentNode'].str.contains('DIV.rllt__details')]
print(df17)
df17.to_csv('shopopening location.csv')
