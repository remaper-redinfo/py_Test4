import csv
f = open('subway1/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

for row in data:
    if data.line_num == 1:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    print(row)
