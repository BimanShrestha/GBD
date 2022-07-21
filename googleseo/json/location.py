
import os, json
import pandas as pd

data = json.load(open('/home/biman/Desktop/ALL_TASK/Task-4/googleseo/json/73.json'))
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
def location(df):
    title = df[df['element'].str.contains('SPAN') & (df['depth'] == 10) & (df['height'] == 20) & (
            df['parentNode'] == "DIV")&(df['width']<396) | (df['attributes.class'] == "OSrXXb")]["text"]

    rating_count1= df[df['element'].str.contains('SPAN') & (df['depth'] == 13) & (df['height'] == 16) & (df['x'] == 272.25)][
        "text"]
    rating_count=rating_count1.str.lstrip('(').str.rstrip(')')

    opening_closing= df[
        df['element'].str.contains('SPAN') & (df['depth'] == 10) & (df['height'] == 60) | df['element'].str.contains(
            'SPAN') & (df['depth'] == 10) & (df['x'] == 228) & (df['height'] == 40) | df['element'].str.contains(
            'SPAN') & (df['depth'] == 23) & (df['parentNode'] == 'DIV') & (df['height'] == 16)]["text"]

    address= df[(df['depth'] == 11)&(df['element'] == "DIV") &(df['parentNode'] == "SPAN")&(df['height'] == 40) | (df['depth'] == 11)&(df['element'] == "DIV") &(df['parentNode'] == "SPAN")&(df['height'] == 60)|(
        df['attributes.class'] == "rllt__details")]["text"]
    rating= df[df['element'].str.contains('DIV') & (df['depth'] == 13) & (df['height'] == 15)]["attributes.aria-label"]
    title = title.values.tolist()
    print(title)
    opening_closing= opening_closing.values.tolist()
    print(opening_closing)
    rating = rating.values.tolist()
    print(rating)
    rating_count =rating_count.values.tolist()
    print(rating_count)
    address= address.values.tolist()
    print(address)
    location_df = pd.DataFrame(columns=['location_title','location_opening_closing' 'location_address', 'location_Rating', 'location_Rating_Count'], index=None)
    location_df.location_title, location_df.location_opening_closing, location_df.location_address = title, opening_closing,  address
    location_df.location_Rating, location_df.location_Rating_Count=rating,rating_count

    location_df.reset_index(drop=True)
    a=vertical(location_df)
    print(a)
    return location_df



location(df)
