import json
import matplotlib.pyplot as plt

jstring = open("weather/myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

jan = []
aug = []

for item in jsonData:
    month = item["date"].split('-')[1]
    if month == '01':
        item["maxTemp"] = float(item["maxTemp"])
        jan.append(item["maxTemp"])
    if month == '08':
        item["maxTemp"] = float(item["maxTemp"])
        aug.append(item["maxTemp"])

# plt.boxplot(jan)
# plt.boxplot(aug)
plt.boxplot([jan, aug])
plt.show()
