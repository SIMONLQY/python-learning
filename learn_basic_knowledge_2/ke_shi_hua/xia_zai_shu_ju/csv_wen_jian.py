import csv
# 1.读取csv的head_row
# 2.处理每行数据
filename = 'weather.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    # 这里就相当于已经读取了第一行，之后reader从第二行开始
    header_row = next(reader)
    print(header_row)
    rows = []
    for row in reader:
        rows.append(row)
    print(rows)


