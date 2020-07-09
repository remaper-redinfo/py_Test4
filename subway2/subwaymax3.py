import csv
import matplotlib.pyplot as plt
f = open('subway2/2020년 06월  교통카드 통계자료2.csv')
data = csv.reader(f)

s_in = [0] * 24
s_out = [0] * 24
for row in data:
    if data.line_num < 3:
        continue
    for i in range(4, 52):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    for j in range(24):
        s_in[j] += row[j*2+4]
        s_out[j] += row[j*2+5]


plt.figure(dpi=150)
plt.rc('font', family='Malgun Gothic')
plt.title('지하철 승하차 정보')
plt.rc('font', family='Malgun Gothic')
plt.plot(s_in, label='승차')
plt.plot(s_out, label='하차')
plt.legend()
plt.xticks(range(24), range(4, 28))
plt.show()
