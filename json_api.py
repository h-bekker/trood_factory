import json

def put(data):
	with open('bd.json', 'r') as f:
		db = json.load(f)
	db.update(data)
	with open('bd.json', 'w') as f:
		json.dump(db, f, ensure_ascii=False)

def take(file):
	with open(file, 'r') as f:
		data = json.load(f)
	return data

def delete(key):
	with open('bd.json', 'r') as f:
		data = json.load(f)
		for k, _ in data.items():
			if k == key:
				del data[key]
				break
	with open('bd.json', 'w') as f:
		json.dump(data, f, ensure_ascii=False)
'''
d={10:"русский","fas":"fas"}
put(d)
ans = take('bd.json')
print(ans)
print(type(ans))
delete("fas")
ans = take('bd.json')
print(ans)
'''