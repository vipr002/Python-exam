# question 4

import random


def main():
    ints = []

    for i in range(10):
        ints.append(random.randint(1, 50))
    print(ints)
    substitute(ints)


def substitute(ints):
    for i in range(10):
        if ints[i] % 5 == 0:
            ints[i] = ints[i] * ints[i]
    print(ints)


main()
