import json
import matplotlib.pyplot as plt

jstring = open("myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

month = [[], [], [], [], [], [], [], [], [], [], [], []]


for item in jsonData:
    mm = int(item["date"].split('-')[1])-1
    # print(mm + " : " + item["maxTemp"])
    month[mm].append(float(item["maxTemp"]))

print(month)

# 기본
# plt.boxplot(month)

# 커스텀
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.boxplot(month, showfliers=False)
plt.show()
