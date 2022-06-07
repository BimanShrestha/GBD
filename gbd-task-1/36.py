import os, json
import pandas as pd

path_to_json = '/home/biman/Desktop/ALL_TASK/Task_1/ALL_DATA'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('36.json')]
final_df = pd.DataFrame()
indexlist = []
final_df_new=[]
# file_name=file_name.split('.')[0]

for file in (json_files):
    final_series = pd.DataFrame()
    data = json.load(open(file))
    df = pd.json_normalize(data["data"])
    df = pd.DataFrame(df)
    title_data_frame = df[df['element'] == "TH"]["text"]
    title_list = list(title_data_frame)
    # print(title_list)
    # title_list.append("")
    # print(title_list)
    data = df[df['element'] == 'TD']
    # data1=data[data['attributes.class']=='SH30Lb']
    # print(data)
    data1 = data[data['parentNode'] == 'TR.sh-osd__offer-row']
    data2 = data1[data1["y"] != 0]
    all_data = data2['text']

    # print(all_data)
    data_list = list(all_data)
    # all_data.to_csv('loop.csv')
    # print(data_list)
    # print(data_list.count("Visit siteOpens in a new window"))


def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res


item = 'Visit siteOpens in a new window'
res = remove_items(data_list, item)
# print(res)
title = []
data = []
# print(len(res))
index_list = []

for file in (json_files):
    file_name=1
    # file_name1 = file.split('.')
    # file_name = file_name1[0]
    if len(data_list) == 0:
        for t in range(len(title_list)):
            title.append(title_list[t])
            data.append("NaN")

    for i in range(len(title_list)):
        j = 0
        while j < len(res):
            title.append(title_list[i])
            if i == j:
                data.append(res[i])
            else:
                data.append(res[i + j])
            j += 4
    for i in range(len(title_list)):
        j = 0
        while j < len(data_list):
            title.append(title_list[i])
            if i == j:
                data.append(res[i])
            index_list.append(str(file_name) + '.' + str(j) + '.' + str(i))
        else:
             # data.append(res[i + j])
             index_list.append(str(file_name) + '.' + str(j // 4) + '.' + str(i))
             j += 4
    # final_df['index'] = indexlist
    print(index_list)
    final_df = list(zip(title, data))
    df = pd.DataFrame(final_df, columns=['title', 'values'])
    df.index=index_list

print(df)
df.to_csv('36.csv')
