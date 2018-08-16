import csv

# 方式一将列头放在第一条，使用writerow写入
datas = [
    ['姓名', '年龄'],
    ['Bob', 14],
    ['Tom', 23],
    ['Jerry', '18']
]

# newline='' 能去掉空行,encoding='utf_8_sig'解决中文乱码问题
with open('./file/test.csv', 'w', newline='', encoding='utf_8_sig') as f:
    # writer = csv.DictWriter(f,header)
    # writer.writerows(datas)
    csv_w = csv.writer(f)
    for row in datas:
        csv_w.writerow(row)

# 方式二写入json格式数据
datas = [
    {'name': 'Bob', 'age': 14},
    {'name': 'Tom', 'age': 14},
    {'name': 'Tom', 'age': 14},
    {'name': 'Monty', 'age': 14}
]

header = ['name', 'age']

with open('./file/test.csv', 'w', newline='', encoding='utf_8_sig') as f:
    csv_f = csv.DictWriter(f, header)
    csv_f.writerows(datas)
