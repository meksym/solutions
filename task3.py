'''
Видалення цифр

Задано натуральне число n. На кожному кроці дозволено
відняти від числа будь яку цифру, яка присутня у заданому числі.

За яку найменшу кількість кроків можна отримати число 0?

Вхідні дані

Одне натуральне число n.

Вихідні дані

Виведіть найменшу кількість кроків, за які можна отримати число 0.
'''


def find(number: int) -> int:
    steps = 0

    while number != 0:
        max_digit = number % 10
        current_number = number // 10

        while current_number != 0:
            digit = current_number % 10
            if digit > max_digit:
                max_digit = digit

            current_number //= 10

        number -= max_digit
        steps += 1

    return steps


def main():
    try:
        number = int(input())
    except ValueError:
        return

    print(find(number))


if __name__ == '__main__':
    main()
