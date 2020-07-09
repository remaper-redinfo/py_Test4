import csv
import matplotlib.pyplot as plt
f = open('subway2/2020년 06월  교통카드 통계자료2.csv')
data = csv.reader(f)

result = []
for row in data:
    if data.line_num < 3:
        continue
    for i in range(4, 52):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    result.append(row[10])

result.sort()
plt.bar(range(len(result)), result)
plt.show()
