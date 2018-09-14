# -*- coding: utf-8 -*-
import csv

csv_file = csv.reader(open('report_rm.csv', 'r', encoding='utf-8'))
# length = open('length.txt', 'w+')
print(type(csv_file))

sum=0
clear_set = []
for item in csv_file:
	if len(item)==40:
		clear_set.append(item)
		sum+=1
	# print(len(item), file=length)


print(sum)
print(len(clear_set))


csv_file2 = open('clear_set.csv','w', newline='', encoding="utf-8") # 设置newline，否则两行之间会空一行
writer = csv.writer(csv_file2)
m = len(clear_set)
for i in range(m):
    writer.writerow(clear_set[i])
csv_file2.close()

print(clear_set[0])

print("done")