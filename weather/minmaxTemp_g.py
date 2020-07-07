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

plt.plot(maxTempList, 'r')
plt.plot(minTempList, 'b')
plt.show()
