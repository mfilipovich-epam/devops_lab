#!/usr/bin/env python3


def check(move):
    x = y = 0
    Up = Down = Left = Right = 0
    for i in range(len(move)):
        if (move[i] == 'U'):
            Up += 1

        elif(move[i] == 'D'):
            Down += 1

        elif(move[i] == 'L'):
            Left += 1

        elif(move[i] == 'R'):
            Right += 1

    x = Right - Left
    y = Up - Down
    return x, y


move = input()
robot_p = check(move)
print (robot_p == (0, 0))
