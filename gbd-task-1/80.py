import json
import pandas as pd
pd.set_option('display.max_columns', 11)
data = json.load(open('/home/biman/Desktop/ALL_TASK/Task_1/80.json'))
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
data2=data1[data1["y"]!=0]
all_data=data2['text']
# print(all_data)
data_list = list(all_data)
# all_data.to_csv('loop.csv')
print(data_list)
print(data_list.count("Visit siteOpens in a new window"))
# data_list.remove('Visit siteOpens in a new window')
# print('updated list:', data_list)
def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res
item = 'Visit siteOpens in a new window'
res = remove_items(data_list, item)
print(res)
title = []
data = []
print(len(res))
index_list=[]
for i in range(len(title_list)):
    j = 0
    while j < len(res):
        title.append(title_list[i])
        if i == j:
            data.append(res[i])
        else:
            data.append(res[i + j])

        j += 4
if len(data_list) == 0:
    for t in range(len(title_list)):
        title.append(title_list[t])
        data.append("NaN")
print(index_list)
final_df = list(zip(title, data))


print(final_df)
print(len(final_df))
df = pd.DataFrame(final_df,columns=['title','values'])
print(df)
df.to_csv('loop80.csv')


