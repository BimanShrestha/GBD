import os, json
import pandas as pd

data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/1.json'))
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




#page Title and Link
df6 = df[df['parentNode'].str.contains('DIV.TbwUpd.NJjxre')&(df['height']==17)&(df['x']==28)]
print(df6)
df6.to_csv('PageLink.csv')
df7 = df[df['element'].str.contains('H3') & df['attributes.class'].str.contains('LC20lb MBeuO DKV0Md') &(df['x']==28)]
print(df7)
df7.to_csv('Pageheading.csv')

#Popular products
df8 = df[df['element'].str.contains('IMG')& (df['depth']==37)&(df['height']==104)]
print(df8)
df8.to_csv('popularproducttitle.csv')

df9 = df[(df['parentNode']==('DIV')) & (df['depth']==39)&(df['height']==16)]
print(df9)
df9.to_csv('popularproductprice.csv')

df10 = df[df['element'].str.contains('DIV') & (df['depth']==37)&(df['height']==14)]
print(df10)
df10.to_csv('popularproductrevcount.csv')

df11 = df[df['element'].str.contains('SPAN') & (df['depth']==40)&(df['height']==12)]
print(df11)
df11.to_csv('popularproductrated.csv')

#Related searches
df12 = df[df['element'].str.contains('A') & (df['depth']==17)&(df['height']==48)]
print(df12)
df12.to_csv('extra.csv')

# adds
df13 = df[df['attributes.class'].str.contains('pymv4e') & (df['depth'] == 22) & (df['height'] == 48)]
df13.to_csv('Shop air filter.csv')
df14 = df[df['parentNode'].str.contains('DIV.T4OwTb') & (df['height'] == 17)]
df14.to_csv('Shop air filter price.csv')
df15 = df[df['parentNode'].str.contains('DIV.pla-extensions-container')]
df15.to_csv('Shop air filter rating count.csv')
df16 = df[df['attributes.class'].str.contains('z3HNkc') & (df['height'] == 11.390625)]
df16.to_csv('Shop air filter rating.csv')









