import json
import matplotlib.pyplot as plt

jstring = open("weather/myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

maxTempList = []
minTempList = []

for item in jsonData:
    item["maxTemp"] = float(item["maxTemp"])
    item["minTemp"] = float(item["minTemp"])
    maxTempList.append(item["maxTemp"])
    minTempList.append(item["minTemp"])

plt.hist(maxTempList, bins=100, color='r', label='max')
plt.hist(minTempList, bins=100, color='b', label='min')
plt.show()
