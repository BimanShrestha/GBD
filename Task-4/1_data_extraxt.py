from itertools import cycle
import pandas as pd
import pprint

data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/1.json'))
df = pd.json_normalize(data["data"])
df = pd.DataFrame(df)
final_series = pd.DataFrame()
df = pd.json_normalize(data["data"])
df = pd.DataFrame(df)
# df2 = df[df['element'].str.contains('SPAN') & (df['x']==28)& (df['depth']==23)]
# print(df2)
# df2.to_csv('popularproduct1.csv')
# print(df)
# df2 = df[df['element'].str.contains('H3') & df['attributes.class'].str.contains('LC20lb MBeuO DKV0Md') & df['x']>0]
# print(df2)
# df2.to_csv('t.csv')
# df3= df[df['element'].str.contains('CITE') & df['attributes.class'].str.contains('iUh30 qLRx3b tjvcx')&df['parentNode'].str.contains('DIV.TbwUpd.NJjxre') & df['height']>0]
# df3.to_csv('t2.csv')
# df4=df[df['parentNode'].str.contains('DIV.yuRUbf')&df['element'].str.contains('DIV')&df['x']>0]
# df4.to_csv('t3.csv')
# df5=df[df['parentNode'].str.contains('DIV.dbg0pd')]
# df5.to_csv('p1.csv')
# df6=df[df['parentNode'].str.contains('DIV.rllt__details')&df['attributes.role'].str.contains('heading')]
# df6.to_csv('p2.csv')
# df7=df[(df['height']==11.390625)&(df['width']==68)&(df['x']==51.46875) ]
# df7.to_csv('p3.csv')
df8 = df[df['attributes.class'].str.contains('pymv4e') & (df['depth'] == 22) & (df['height'] == 48)]
df8.to_csv('Shop air filter.csv')
df9 = df[df['parentNode'].str.contains('DIV.T4OwTb') & (df['height'] == 17)]
df9.to_csv('Shop air filter price.csv')
df10 = df[df['parentNode'].str.contains('DIV.pla-extensions-container')]
df10.to_csv('Shop air filter rating count.csv')
df11 = df[df['attributes.class'].str.contains('z3HNkc') & (df['height'] == 11.390625)]
df11.to_csv('Shop air filter rating.csv')








