import csv
f = open('subway1/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

mx = 0
rate = 0
mx_row = []
mx_list = [0,0]

for row in data:
    if data.line_num == 1:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])
    if row[6] != 0:
        rate = row[4]/row[6]
        if rate > mx:
            mx = rate
            mx_row = row
            mx_row_num = data.line_num
            mx_list[0] = mx_row_num

print("1등 출력 : ")
print(mx_row)

f = open('subway1/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

mx = 0
rate = 0
mx_row = []

for row in data:
    if data.line_num == 1 or data.line_num == mx_list[0]:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])
    if row[6] != 0:
        rate = row[4]/row[6]
        if rate > mx:
            mx = rate
            mx_row = row
            mx_row_num = data.line_num
            mx_list[1] = mx_row_num

print("2등 출력 : ")
print(mx_row)

f = open('subway1/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

mx = 0
rate = 0
mx_row = []

for row in data:
    if data.line_num == 1 or data.line_num == mx_list[0] or data.line_num == mx_list[1]:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])
    if row[6] != 0:
        rate = row[4]/row[6]
        if rate > mx:
            mx = rate
            mx_row = row

print("3등 출력 : " )
print(mx_row)
