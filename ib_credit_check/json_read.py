import json
with open('firm_list.json', 'r') as f:
	dic = json.load(f)

v = dic['firm']
for f in v:
	print(f)