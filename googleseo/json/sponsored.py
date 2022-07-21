import os, json
import pandas as pd

data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/71.json'))
df = pd.json_normalize(data["data"])
df = pd.DataFrame(df)
final_series = pd.DataFrame()
def vertical(value):
    datas = []
    column = len(value.columns)
    for i in range(column + 1):
        column_data = value.iloc[:, i - 1]
        datas = pd.Series(datas.append(column_data))
    return (datas)

# sponsored

def sponsored(df):
    title = df[df['attributes.class'].str.contains('Wk3jdb tNxQIb') & (df['element'] == "DIV")]["text"]
    price = df[df['attributes.class'].str.contains('pSNTSe') & (df['element'] == "DIV")]["text"]
    details = df[df['attributes.class'].str.contains('BZuDuc') & (df['element'] == "DIV")]["text"]
    title = title.values.tolist()
    print(title)
    price = price.values.tolist()
    print(price)
    details = details.values.tolist()
    print(details)
    sponsored_df = pd.DataFrame(columns=['sponsored_title','sponsored_details', 'sponsored_price'], index=None)
    sponsored_df.sponsored_title,sponsored_df.sponsored_details,sponsored_df.sponsored_price = title, details,price
    sponsored_df.reset_index(drop=True)

    print(sponsored_df)
    s=pd.DataFrame(sponsored_df)
    headers = pd.Series(df.columns.values.tolist())
    s.to_csv("s.csv")
    a = vertical(sponsored_df)
    print(a)


sponsored(df)

df_all_rows = pd.concat([df_SN7577i_a, df_SN7577i_b], ignore_index=True)








