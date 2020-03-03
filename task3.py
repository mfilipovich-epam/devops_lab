#!/usr/bin/env python3

fact = 1
# print ("number:")
n = int(input())

for i in range(1, n + 1):
    fact *= i
print(fact)
# if n != 0 & n != 1 & n > 1:
#    for i in range(1, n+1):
#       fact =* i
#       print ("The factorial of " +str(n), "is :")

# elif n == 0 or n == 1:
#     print("The factorial of " +str(n), "is :")
#     print("1")
# elif n < 0:
#     print("Wrong input for Number")
