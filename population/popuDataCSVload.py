import csv
f = open('202006_202006_연령별인구현황_월간.csv')
data = csv.reader(f)

for row in data:
    print(row)
