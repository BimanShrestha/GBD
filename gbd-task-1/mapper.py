import os, json
import pandas as pd

path_to_json = '/home/biman/Desktop/ALL_TASK/Task_1'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)
print(len(json_files))
fname = []
number = []
n=1
for file in json_files:
    names=file
    print(names)
    number.append(n)
    n += 1
    fname.append(names)
# file_name = json_files[0:10].split(".")


map = list(zip(fname, number))
map_df = pd.DataFrame(map, columns=['filename','newindex'])
map_df.to_csv('mapper.csv', index=False)
