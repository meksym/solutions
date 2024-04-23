'''
Число що зменшується

Над цілим числом можна здійснювати наступні операції:

- Якщо число ділиться на 3, то розділити його на 3;
- Якщо число ділиться на 2, то розділити його на 2;
- Відняти 1.

За заданоим натуральним числом n знайти найменшу
кількість операцій, після виконання яких отримаємо 1.

Вхідні дані

Кожний рядок містить одне натуральне число n.

Вихідні дані

Для кожного значення n в окремому рядку вивести найменшу кількість
операцій, після виконання яких отримаємо 1.
'''
import sys


def find(number: int) -> int:
    queue = [(0, number)]
    visited = set()

    while queue:
        operations, num = queue.pop(0)

        if num == 1:
            return operations

        visited.add(num)
        operations += 1

        if num % 3 == 0 and num // 3 not in visited:
            queue.append((operations, num // 3))
        if num % 2 == 0 and num // 2 not in visited:
            queue.append((operations, num // 2))
        if num - 1 not in visited:
            queue.append((operations, num - 1))


def main():
    results = []

    for line in sys.stdin.readlines():
        if line:
            number = int(line)
            results.append(find(number))

    print(*results, sep='\n')


if __name__ == '__main__':
    main()
