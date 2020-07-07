import json

jstring = open("weather/myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

# print(type(jsonData))
# print(jsonData)

for item in jsonData:
    item["maxTemp"] = float(item["maxTemp"])
    item["minTemp"] = float(item["minTemp"])
    # print(item)

maxTemp = 0
maxTempdate = ""

for item in jsonData:
    if maxTemp > item["minTemp"]:
        maxTempdate = item["date"]
        maxTemp = item["minTemp"]

print(maxTemp)
print(maxTempdate)
