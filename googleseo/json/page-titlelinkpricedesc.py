# page Title and Link
df6 = df[df['element'].str.contains('DIV') & (df['height'] == 22) & (df['parentNode'] == 'A') | (df[
                                                                                                     'attributes.class'] == "qzEoUe") | (
                 df[
                     'attributes.class'] == "TbwUpd") & df['element'].str.contains('DIV') & (df['x'] == 28)][
    "text"]
print(df6)
df6.to_csv('PageLink.csv', index=False)

df7 = df[df['element'].str.contains('H3') & (df['height'] == 26) & (df['parentNode'] == 'A') | df[
    'attributes.class'].str.contains('CCgQ5 MUxGbd v0nnCb aLF0Z OSrXXb') | (df['height'] == 52) & (
                 df['attributes.class'] == "zBAuLc l97dzf") | (df[
                                                                   'attributes.class'] == "LC20lb MBeuO DKV0Md") & (
                 df['element'] == "H3") & (df['x'] == 28)]["text"]
print(df7)
df7.to_csv('Pageheading.csv', index=False)

df8 = df[df['element'].str.contains('DIV') & (df['height'] == 44) & (df['depth'] == 11) | (
        df['attributes.class'] == "w1C3Le") | df['element'].str.contains('DIV') & (df['depth'] == 6) & (
                 df['height'] == 46) & (df['attributes.class'] == "kCrYT") | df['element'].str.contains('DIV') & (
                 df['height'] == 88) & (df['depth'] == 11) | (df[
                                                                  'attributes.class'] == "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf") & (
                 df['x'] == 28)]["text"]
print(df8)
df8.to_csv('Pagedetails.csv', index=False)

df9 = df[df['element'].str.contains('DIV') & (df['height'] == 15) & (df['depth'] == 13) & (df['x'] == 247.71875) | (
        df['attributes.class'] == "Hk2yDb KsR1A") & df['element'].str.contains('DIV') & (df['depth'] == 10)][
    "attributes.aria-label"]
print(df9)
df9.to_csv('Pagerating.csv')

df10 =
    df[df['element'].str.contains('SPAN') & (df['depth'] == 13) & (df['height'] == 16) & (df['x'] == 316.609375) | (
            df['depth'] == 13) & df['element'].str.contains('SPAN') & (df['x'] == 316.609375)]["text"]
print(df10)
df10.to_csv('pageratingcount.csv')

df23 = df[df['element'].str.contains('SPAN') & (df['depth'] == 12) & (df['attributes.class'] == "xUrNXd UMOHqf") & (
        df['width'] == 42.828125)]["text"]
print(df23)
df23.to_csv('pageratingprice.csv', index=False)