#!/usr/bin/env python3

sum = 0
count = 0
s_list = {}

x = input()

for i in range(int(x)):
    inp_st = input().split()
    name = inp_st[0]
    marks = inp_st[1:]
    for numbers in marks:
        sum += float(numbers)
        count += 1
    s_list[name] = sum / count

user = input()
print("{:.2f}".format(s_list.get(user)))
