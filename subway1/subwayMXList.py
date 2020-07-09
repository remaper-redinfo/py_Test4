import csv
f = open('subway1/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

rate = 0.0
mx_list = []
for row in data:
    if data.line_num == 1:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6]) > 10000:
        rate = row[4]/(row[4]+row[6])
        if rate > 0.90:
            mx = rate
            mx_list.append(row)

print(mx)
print(mx_list)
