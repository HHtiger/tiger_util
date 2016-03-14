#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    筛选项目日志中sql执行语句并还原
"""

f = open("log", "r", -1, 'utf-8')
res_list = []
lines = f.readlines()  # 读取全部内容
count = 0
for index, line in enumerate(lines):
    line = line.replace('\n', '')
    if 'Executing Statement' in line:
        count += 1
        # print('--start-------%d----------' % count)
        res_list.append('--start-------%d----------\n' % count)
        if line.find('?') != -1:
            next_line = lines[index + 1]
            if 'Parameters:' not in next_line:
                next_line = lines[index + 2]
            parameters = next_line[next_line.find('Parameters: [') + len('Parameters: ['):len(next_line) - 2].split(',')
            for i in parameters:
                line = line.replace('?', '\'' + i.strip(' ') + '\'', 1)
        # print(line[line.find('Executing Statement:') + len('Executing Statement:'):].lstrip() + ';')
        # print('--end---------%d----------' % count)
        res_list.append(line[line.find('Executing Statement:') + len('Executing Statement:'):].lstrip() + ';\n')
        res_list.append('--end---------%d----------\n' % count)

res = open("res", "w", -1, 'utf-8')
res.writelines(res_list)
res.close()
f.close()
print('done! the result save as 【res】')
