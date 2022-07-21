import os, json
import pandas as pd

# path_to_json ='/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json'
# json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('81.json')]
# data = json_files
data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/71.json'))
df = pd.json_normalize(data["data"])
df = pd.DataFrame(df)
final_series = pd.DataFrame()
# df = pd.json_normalize(data["data"])
# df = pd.DataFrame(df)
df.to_csv('94.csv')
# for file in (json_files):
#     final_series = pd.DataFrame()
#     data = json.load(open(file))
#     df = pd.json_normalize(data["data"])
#     df = pd.DataFrame(df)
# page Title and Link
df6 = df[df['element'].str.contains('DIV') & (df['height'] == 22) & (df['parentNode'] == 'A') | (df[
                                                                                                     'attributes.class'] == "qzEoUe") | (
                 df[
                     'attributes.class'] == "TbwUpd") & df['element'].str.contains('DIV') & (df['x'] == 28)][
    "text"]
print(len(df6))
df6.to_csv('PageLink.csv', index=False)

df7 = df[df['element'].str.contains('H3') & (df['height'] == 26) & (df['parentNode'] == 'A') | df[
    'attributes.class'].str.contains('CCgQ5 MUxGbd v0nnCb aLF0Z OSrXXb') | (df['height'] == 52) & (
                 df['attributes.class'] == "zBAuLc l97dzf") | (df[
                                                                   'attributes.class'] == "LC20lb MBeuO DKV0Md") & (
                 df['element'] == "H3") & (df['x'] == 28)]["text"]
print(len(df7))
df7.to_csv('Pageheading.csv', index=False)

# df8 = df[df['element'].str.contains('DIV') & (df['height'] == 44) & (df['depth'] == 11) | (
#         df['attributes.class'] == "w1C3Le") | df['element'].str.contains('DIV') & (df['depth'] == 6) & (
#                  df['height'] == 46) & (df['attributes.class'] == "kCrYT") | df['element'].str.contains('DIV') & (
#                  df['height'] == 88) & (df['depth'] == 11) | (df[
#                                                                   'attributes.class'] == "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf") & (
#                  df['x'] == 28)|df['element'].str.contains('DIV') & (df['height'] == 66) & (df['depth'] == 11)]
df8 = df[
    df['element'].str.contains('DIV') & (df['x'] == 164) & (df['depth'] == 6) & (df['attributes.class'] == "kCrYT") & (
                df['parentNode'] == 'DIV.ZINbbc.luh4tb.xpd.O9g5cc.uUPGi') | df['element'].str.contains('DIV') & (
                df['depth'] == 7) & (df['parentNode'] == 'DIV.ZINbbc.luh4tb.O9g5cc.uUPGi') & (df['height'] == 45)]
print(len(df8))
df8.to_csv('Pagedetails.csv', index=False)

df9 = df[df['element'].str.contains('DIV') & (df['height'] == 15) & (df['depth'] == 13) & (df['x'] == 247.71875) | (
        df['attributes.class'] == "Hk2yDb KsR1A") & df['element'].str.contains('DIV') & (df['depth'] == 10)][
    "attributes.aria-label"]
print(len(df9))
df9.to_csv('Pagerating.csv')

df10 = df[df['element'].str.contains('SPAN') & (df['depth'] == 13) & (df['height'] == 16) & (df['x'] == 316.609375) | (
        df['depth'] == 13) & df['element'].str.contains('SPAN') & (df['x'] == 316.609375)]["text"]
print(len(df10))
df10.to_csv('pageratingcount.csv')

df23 = df[df['element'].str.contains('SPAN') & (df['depth'] == 12) & (df['attributes.class'] == "xUrNXd UMOHqf") & (
        df['width'] == 42.828125)]["text"]
print(len(df23))
df23.to_csv('pageratingprice.csv', index=False)

# location
df2 = df[df['element'].str.contains('SPAN') & (df['depth'] == 10) & (df['height'] == 20) & (
        df['parentNode'] == "DIV")&(df['width']<396) | (df['attributes.class'] == "OSrXXb")]["text"]

print(len(df2))
df2.to_csv('shopname.csv', index=False)
df4 = df[df['element'].str.contains('SPAN') & (df['depth'] == 13) & (df['height'] == 16) & (df['x'] == 272.25)][
    "text"]
print(len(df4))
df4.to_csv('shopreviewcount.csv', index=False)
df5 = df[
    df['element'].str.contains('SPAN') & (df['depth'] == 10) & (df['height'] == 60) | df['element'].str.contains(
        'SPAN') & (df['depth'] == 10) & (df['x'] == 228) & (df['height'] == 40) | df['element'].str.contains(
        'SPAN') & (df['depth'] == 23) & (df['parentNode'] == 'DIV') & (df['height'] == 16)]["text"]
print(len(df5))
df5.to_csv('shopopening closing.csv', index=False)
df17 = df[(df['depth'] == 11)&(df['element'] == "DIV") &(df['parentNode'] == "SPAN")&(df['height'] == 40) | (df['depth'] == 11)&(df['element'] == "DIV") &(df['parentNode'] == "SPAN")&(df['height'] == 60)|(
        df['attributes.class'] == "rllt__details")]["text"]
print(len(df17))
df17.to_csv('shopopening location.csv', index=False)
df3 = df[df['element'].str.contains('DIV') & (df['depth'] == 13) & (df['height'] == 15)]["attributes.aria-label"]
print(df3)
df3.to_csv('shoprating.csv', index=False)

# sponsored
df18 = df[df['attributes.class'].str.contains('Wk3jdb tNxQIb') & (df['element'] == "DIV")]["text"]
print(len(df18))
df18.to_csv('sponsoredtitle.csv', index=False)
df19 = df[df['attributes.class'].str.contains('pSNTSe') & (df['element'] == "DIV")]["text"]
print((df19))
df19.to_csv('sponsoredprice.csv', index=False)
df20 = df[df['attributes.class'].str.contains('BZuDuc') & (df['element'] == "DIV")]["text"]
print(len(df20))
df20.to_csv('sponsoreddetails.csv', index=False)

# Related searches
df21 = df[df['attributes.class'].str.contains('gGQDvd iIWm4b') & (df['element'] == "DIV")]["text"]
print(len(df21))
df21.to_csv('Related searches title.csv', index=False)
df22 = df[df['attributes.class'].str.contains('Q71vJc') & (df['element'] == "A")]["attributes.href"]
print(len(df22))
df22.to_csv('Related searches link.csv', index=False)
# linksearch=
# linktitle=
# # creating list  kk
# relatedsearchestitle=df21.values.tolist()
# relatedsearchlink=df22.values.tolist()
# final_df = list(zip(, relatedsearchlink))
# print(relatedsearchlink)
# print(relatedsearchestitle)
print(final_df)
