import os, json
import pandas as pd

data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/80.json'))
df = pd.json_normalize(data["data"])
df = pd.DataFrame(df)
final_series = pd.DataFrame()


def relatedsearchs(df):
    # Related searches
    title = df[df['attributes.class'].str.contains('gGQDvd iIWm4b') & (df['element'] == "DIV")]["text"]
    link = df[df['attributes.class'].str.contains('Q71vJc') & (df['element'] == "A")]["attributes.href"]
    title = title.values.tolist()
    print(title)
    links = link.values.tolist()
    print(links)
    related_df = pd.DataFrame(columns=['related_title','related_link'],index=None)
    related_df.related_title, related_df.related_link = title, links
    related_df.reset_index(drop=True)
    print(related_df)
    return related_df
relatedsearchs(df)




