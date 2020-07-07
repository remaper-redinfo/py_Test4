import csv
f = open('popuMiniProject/202006_202006_연령별인구현황_월간_전국.csv')
data = csv.reader(f)

# for row in data:
#     if '서울특별시 성북구 안암동(1129060000)' == row[0]:
#         print(row)

# for row in data:
#     if '장위' in row[0]:
#         print(row)

# for row in data:
#     if '성북구' in row[0]:
#         for i in row[3:]:
#             print(i)

mn = 10000
result = []
result_name = ''

home = []
home_name = '중곡제3동'
home_linenum = 0
for row in data:
    if home_name in row[0]:
        home_linenum = data.line_num
        for i in row[3:]:
            i = i.replace(",", "")
            home.append(int(i))

f = open('popuMiniProject/202006_202006_연령별인구현황_월간_전국.csv')
data = csv.reader(f)

for row in data:
    if data.line_num == 1 or data.line_num == home_linenum:
        continue
    away = []
    res = [0] * 101
    for i in row[3:]:
        i = i.replace(",", "")
        away.append(int(i))

    for i in range(0, 101):
        res[i] = home[i]-away[i]

    sumRes = sum(res)
    sumRes = abs(sumRes)

    if(mn > sumRes):
        result_name = row[0]
        mn = sumRes
        result = away

print(result_name)
print(result)
print(mn)
