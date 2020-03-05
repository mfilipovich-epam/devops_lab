#!/usr/bin/env python3

sum = 0
s_list = {}

x = input()

for i in range(int(x)):
    inp_st = input().split()
    name = inp_st[0]
    marks = inp_st[1:]
    sum = 0
    for numbers in marks:
        sum += float(numbers)
    s_list[name] = sum / 3

user = input()
print("{:.2f}".format(s_list.get(user)))
