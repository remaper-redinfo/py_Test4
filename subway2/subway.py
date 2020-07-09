import csv
f = open('subway2/2020년 06월  교통카드 통계자료2.csv')
data = csv.reader(f)

for row in data:
    if data.line_num < 3:
        continue
    len(row)
    for i in range(4, 52):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    # row[4:] = map(int, row[4:])
print(row)    
