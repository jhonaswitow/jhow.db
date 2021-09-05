import json

def get(key):
		with open("jhowdb.json", "r") as f:
			data = json.load(f)
			return data[key]

			if data[key] == None:
				with open("jhowdb.json", "w") as b:
					json.dump({key: 0}, b, indent=2)
					return data[key]
		
def set(key, option):
				d = { key: option }
				with open("jhowdb.json", "w") as f:
				 json.dump(d, f, indent=2)
				 return True
