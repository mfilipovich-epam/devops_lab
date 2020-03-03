#!/usr/bin/env python3

l1 = input().split()
l2 = input().split()


def compare_list(l1, l2):
    for i in range(len(l1)):
        l1[i] = int(l1[i])
    for i in range(len(l2)):
        l2[i] = int(l2[i])
    if len(l1) != len(l2):
        diff = len(l1) - len(l2)
        for i in range(diff):
            l2.append(None)
    return dict(zip(l1, l2))


print(compare_list(l1, l2))
