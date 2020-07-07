import json

jstring = open("weather/myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

print(type(jsonData))
print(jsonData)
