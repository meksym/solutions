'''
Реалізуйте рекурсивну функцію:

f(n) =
    0, n = 0
    f(n - 1) + n, n > 0
'''
import sys


def func(number: int) -> int:
    assert number >= 0

    if number == 0:
        return number

    return func(number - 1) + number


def main():
    input_number = int(input())
    print(func(input_number))


if __name__ == '__main__':
    sys.setrecursionlimit(10**4)
    main()
