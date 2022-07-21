# location
df2 = df[df['element'].str.contains('SPAN') & (df['depth'] == 10) & (df['height'] == 20) & (
        df['parentNode'] == "DIV") | (df['attributes.class'] == "OSrXXb")]["text"]
print(df2)
df2.to_csv('shopname.csv', index=False)
df4 = df[df['element'].str.contains('SPAN') & (df['depth'] == 13) & (df['height'] == 16) & (df['x'] == 272.25)][
    "text"]
print(df4)
df4.to_csv('shopreviewcount.csv', index=False)
df5 = df[
    df['element'].str.contains('SPAN') & (df['depth'] == 10) & (df['height'] == 60) | df['element'].str.contains(
        'SPAN') & (df['depth'] == 10) & (df['x'] == 228) & (df['height'] == 40) | df['element'].str.contains(
        'SPAN') & (df['depth'] == 23) & (df['parentNode'] == 'DIV') & (df['height'] == 16)]["text"]
print(df5)
df5.to_csv('shopopening closing.csv', index=False)
df17 = df[df['attributes.class'].str.contains('BNeawe tAd8D AP7Wnd') & (df['depth'] == 11) | (
        df['attributes.class'] == "rllt__details")]["text"]
print(df17)
df17.to_csv('shopopening location.csv', index=False)
# df3 = df[df['element'].str.contains('DIV') & (df['depth'] == 13) & (df['height'] == 15)]
# print(df3)
# df3.to_csv('shoprating.csv', index=False)