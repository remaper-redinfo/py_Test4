import csv
import matplotlib.pyplot as plt
f = open('subway2/2020년 06월  교통카드 통계자료2.csv')
data = csv.reader(f)

mx = [0] * 24
mx_station = [''] * 24
for row in data:
    if data.line_num < 3:
        continue
    for i in range(4, 52):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    for j in range(24):
        a = row[j*2+4]
        if a > mx[j]:
            mx[j] = a
            mx_station[j] = row[3]+'('+str(j+4)+')'

# print(mx_station)
# print(mx)

plt.figure(dpi=150)
plt.rc('font', family='Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation=90)
plt.show()
