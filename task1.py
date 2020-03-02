#!/usr/bin/env python3

sum = 0
count = 0
s_list = {}
# print  ("How many students: ")
x = int(input())
# print ("Enter " +str(x), " times information for student ")
for i in range(int(x)):
    # print("Enter student's name, Math's mark, Phis's mark, Chem's mark:")
    inp_st = input()
    stud = inp_st.split()
    name = stud[0]
    marks = stud[1:]
    for numbers in marks:
        sum += float(numbers)
        count += 1
        s_list[name] = sum/count

# print ("choose student ")
user = input()
print(s_list.get(user))
