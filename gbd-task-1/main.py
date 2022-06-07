import os, json
import pandas as pd


path_to_json = '/home/biman/Desktop/ALL_TASK/Task_1/ALL_DATA'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
indexlist = []
final_df =pd.DataFrame()


for file in (json_files):
    
    final_series =pd.DataFrame()    

    data = json.load(open(file))
    df = pd.json_normalize(data["data"])
    df = pd.DataFrame(df)
    # print(df)

    title_df = df[df['element']=="TH"]
    title_df = title_df[["text"]]
    title_ser = title_df['text'].squeeze()
    titles = title_ser.tolist()
    titles.append("")

    df2 = df[df['element'].str.contains('TD') & df['attributes.class'].str.contains('SH30Lb')]
    unique_y = df2['y'].unique()

    l = len(unique_y)
    df_split = [None] * l
    series = [None] * l

    for i in range(l):
        df_split[i] = df2[df2['y'] == unique_y[i]]
        df_split[i] = df_split[i][["text"]]
        df_split[i] = df_split[i].reset_index(drop=True)
        df_split[i] = df_split[i].replace('Opens in a new window','', regex=True)
        series[i] = df_split[i]['text'].squeeze()
        # print("\n\n")
        # print(series[i])

    df_new=pd.concat(series,axis=1).T
    df_new = df_new.reset_index(drop=True)

    df_new.columns = titles
    df_new.head()

    df_new["Total price"] = df_new["Total price"].str.split('Item').str[0]

    x = file.split(".")
    x = x[0]
    x_to_csv = x + ".csv"

    # print(df_new["Total price"])
    df_new.to_csv(x_to_csv)
    # df.to_csv("7.csv")




################################################################################
    pd.set_option('display.max_rows', 1000)

    df_new = df_new.iloc[: , :-1]
    total_col = len(df_new.columns)
    series2 = [None] * total_col

    for i in range(total_col):
        series2[i] = df_new.iloc[:,i]
        series2[i].to_frame()
        title_list = [series2[i].name] * len(df_new)
        series_title = pd.Series( title_list )
        # print(series_title)
        series2[i].name = None
        series2[i] = pd.concat([series_title, series2[i]], axis=1)
        # print(df2)

        for j in range(len(df_new)):
            indexlist.append(str(x) + '.' + str(i) + '.' + str(j))

        # print(series2[i])

    for i in range(total_col):
        final_series = final_series.append(series2[i], ignore_index = True)

    # print(final_series)

    xa_to_csv = x + "a.csv"
    final_series.to_csv(xa_to_csv)

    final_df = final_df.append(final_series, ignore_index = True)
    
final_df['index'] = indexlist
# print(indexlist)
# print(len(final_df))
# print(len(indexlist))
final_df = final_df.set_index("index")
# print(final_df)
final_df.to_csv("main.csv")

