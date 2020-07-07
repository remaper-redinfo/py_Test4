import csv
f = open('population/202006_202006_연령별인구현황_월간_남여.csv')
data = csv.reader(f)

for row in data:
    print(row)
