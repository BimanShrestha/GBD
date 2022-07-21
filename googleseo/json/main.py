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

def organic_page(df):

        pagetitles = df[df['element'].str.contains('H3') & (df['height'] == 26) & (df['parentNode'] == 'A') | df[
            'attributes.class'].str.contains('CCgQ5 MUxGbd v0nnCb aLF0Z OSrXXb') | (df['height'] == 52) & (
                                df['attributes.class'] == "zBAuLc l97dzf") | (df[
                                                                                  'attributes.class'] == "LC20lb MBeuO DKV0Md") & (
                                df['element'] == "H3") & (df['x'] == 28)]["text"]
        pagelink = df[df['element'].str.contains('DIV') & (df['height'] == 22) & (df['parentNode'] == 'A') | (df[
                                                                                                                  'attributes.class'] == "qzEoUe") | (
                              df[
                                  'attributes.class'] == "TbwUpd") & df['element'].str.contains('DIV') & (
                                  df['x'] == 28)][
            "text"]
        pagedescription = df[
            df['element'].str.contains('DIV') & (df['x'] == 164) & (df['depth'] == 6) & (
                        df['attributes.class'] == "kCrYT") & (
                    df['parentNode'] == 'DIV.ZINbbc.luh4tb.xpd.O9g5cc.uUPGi') | df['element'].str.contains('DIV') & (
                    df['depth'] == 7) & (df['parentNode'] == 'DIV.ZINbbc.luh4tb.O9g5cc.uUPGi') & (df['height'] == 45)]["text"]
        pagePrice = \
        df[df['element'].str.contains('SPAN') & (df['depth'] == 12) & (df['attributes.class'] == "xUrNXd UMOHqf") & (
                df['width'] == 42.828125)]["text"]
        pageRatingCount = \
        df[df['element'].str.contains('SPAN') & (df['depth'] == 13) & (df['height'] == 16) & (df['x'] == 316.609375) | (
                df['depth'] == 13) & df['element'].str.contains('SPAN') & (df['x'] == 316.609375)]["text"]
        pageRating = \
        df[df['element'].str.contains('DIV') & (df['height'] == 15) & (df['depth'] == 13) & (df['x'] == 247.71875) | (
                df['attributes.class'] == "Hk2yDb KsR1A") & df['element'].str.contains('DIV') & (df['depth'] == 10)][
            "attributes.aria-label"]

        title = pagetitles.values.tolist()
        print(title)
        links = pagelink.values.tolist()
        print(links)
        description = pagedescription.values.tolist()
        print(description)
        price = pagePrice.values.tolist()
        if len(price)==0:
            price=['N/A']*len(title)
        print(price)
        rating = pageRating.values.tolist()
        if len(rating)==0:
            rating=['N/A']*len(title)
        print(rating)
        ratingcount = pageRatingCount.values.tolist()

        if len(ratingcount)==0:
            ratingcount=['N/A']*len(title)
        print(ratingcount)


        organic_df = df.fillna('', inplace=True)
        organic_df=pd.DataFrame(columns=['organic_title','organic_Link','organic_description','Organic_Rating','Organic_Rating_Count','organic_price'],index=None)





        organic_df.organic_title,organic_df.organic_Link,organic_df.organic_description = title,links,description

        organic_df.Organic_Rating, organic_df.Organic_Rating_Count, organic_df.organic_price = rating, ratingcount, price

        organic_df.reset_index(drop=True)


        print(organic_df)


        return organic_df


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
    if len( opening_closing) == 0:
        opening_closing = ['N/A'] * len(title)
    print(opening_closing)

    rating = rating.values.tolist()
    print(rating)
    rating_count =rating_count.values.tolist()
    print(rating_count)
    address= address.values.tolist()
    if len(address) == 0:
        address = ['N/A'] * len(title)

    print(address)
    location_df = pd.DataFrame(columns=['location_title','location_address', 'location_Rating', 'location_Rating_Count'], index=None)
    location_df.location_title, location_df.location_opening_closing, location_df.location_address = title, opening_closing,  address
    location_df.location_Rating, location_df.location_Rating_Count=rating,rating_count
    print(location_df)
    location_df.reset_index(drop=True)

    # location_df.reset_index(drop=True)
    # a=vertical(location_df)
    # print(a)
    return location_df

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
    return sponsored_df
    # s=pd.DataFrame(sponsored_df)
    # headers = pd.Series(df.columns.values.tolist())
    # s.to_csv("s.csv")
    # a = vertical(sponsored_df)
    # print(a)

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

    print(related_df)
    related_df.reset_index(drop=True)
    return related_df




relatedsearchs(df)
location(df)
sponsored(df)
organic_page(df)
def main():
    df_all_rows = pd.concat([ relatedsearchs(df), sponsored(df), location(df),organic_page(df)])
    print(df_all_rows)

    df_all_rows.to_csv("all.csv", index=None)
main()