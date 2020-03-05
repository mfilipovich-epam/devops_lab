#!/usr/bin/env python3


def compare_list(l1, l2):
    if len(l1) != len(l2):
        diff = len(l1) - len(l2)
        for i in range(diff):
            l2.append(None)
    return dict(zip(l1, l2))


if __name__ == '__main__':
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
#    print(compare_list(l1, l2))
