#!/usr/bin/bash

import re

N = int(input())

li = []

weights = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
check_list= ['1','0','X','9','8','7','6','5','4','3','2']

for i in range(N):
    row_line = input()
    main_str = row_line[0:17]
    check_char = row_line[17]
    if re.match('\d{17}',main_str):
        tmp_list = [int(x) for x in main_str]
        sum = 0
        for i in range(17):
            sum = sum + tmp_list[i] * weights[i]
        index = sum % 11
        if check_list[index] != check_char:
            li.append(row_line)

    else:
        li.append(row_line)

if len(li) == 0:
    print("All passed")
else:
    for string in li:
        print(string)
