import csv
f = open('subway2/2020년 06월  교통카드 통계자료2.csv')
data = csv.reader(f)

mx = 0
mx_station = ''
for row in data:
    if data.line_num < 3:
        continue
    for i in range(4, 52):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    # if sum(row[10:15:2]) > mx:
    #     mx = sum(row[10:15:2])
    #     mx_station = row[3] + '(' + row[1] + ')'

    # if sum(row[11:16:2]) > mx:
    #     mx = sum(row[11:16:2])
    #     mx_station = row[3] + '(' + row[1] + ')'

    s_t = 9
    e_t = 18
    a = sum(row[(4+(s_t-4)*2):(4+(e_t-4)*2):2])
    if a > mx:
        mx = a
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)
