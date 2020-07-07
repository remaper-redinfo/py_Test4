import json
import matplotlib.pyplot as plt

jstring = open("weather/myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

maxTempList = []

for item in jsonData:
    if item["date"].split('-')[2] == '01':
        item["maxTemp"] = float(item["maxTemp"])
        maxTempList.append(item["maxTemp"])

plt.plot(maxTempList, 'r')
plt.show()
