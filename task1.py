'''
Перестановки

Задано рядок, який складається з M (2 ≤ M ≤ 8) попарно відмінних
символів (літери латинського алфавіту та цифри). Потрібно вивести
всі перестановки символів заданого рядка в алфавітному порядку.

Вхідні дані

У першому рядку файла знаходиттся заданий рядок.

Вихідні дані

Вивести у кожному рядку файла по одній перестановці.
'''


def permutations(string: str) -> list[str]:
    if len(string) == 1:
        return [string]

    result = []

    for i, char in enumerate(string):
        string_without_char = string[:i] + string[i+1:]

        for permutation in permutations(string_without_char):
            result.append(char + permutation)

    return result


def merge(array: list[str], start: int, middle: int, end: int):
    assert start < middle < end

    right = middle

    for left in range(start, end - 1):
        if left == right:
            break

        if array[left] > array[right]:
            current = array[right]

            for i in range(right, left, -1):
                array[i] = array[i - 1]

            array[left] = current
            right += 1


def sort(array: list[str], start: int, end: int):
    assert start < end

    length = end - start

    if length == 0 or length == 1:
        return

    if length == 2:
        if array[start] > array[start + 1]:
            array[start], array[start + 1] = array[start + 1], array[start]
        return

    middle = start + int(length / 2)

    sort(array, start, middle)
    sort(array, middle, end)
    merge(array, start, middle, end)


def main():
    array = permutations(input())
    sort(array, 0, len(array))
    print(*array, sep='\n')


if __name__ == '__main__':
    main()
