import json
f = open('config.json')
data = json.load(f)
print(data['name'])
for i in data['main_content']:
    print(i['category'])
    print(i['content'])
    for da in i['content']:
        print(da['field'])
        print(da['xpath'])



f.close()