import csv
f = open('popuMiniProject/202006_202006_연령별인구현황_월간_전국.csv')
data = csv.reader(f)

home = []
home_name = '중곡제3동'
for row in data:
    if home_name in row[0]:
        for i in row[3:]:
            i = i.replace(",", "")
            home.append(int(i))

print(home)

home = []
home_name = '중곡제3동'
for row in data:
    if home_name in row[0]:
        for i in row[3:]:
            i = i.replace(",", "")
            home.append(int(i))

print(home)
