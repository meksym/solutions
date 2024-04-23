'''
Морозиво

Степан та його друзі поїхали у відпустку до Ужляндії. Ховаючись від
спеки, вони вирішили придбати морозива. Є n смаків морозива,
пронумерованих від 1 до n. Оскільки деякі смаки несумісні, таких пар
треба уникнути, інакше буде дуже неприємний смак. Степан хоче знати
скільки існує способів вибрати три різні смаки морозива так, щоб серед
них не було жодної несумісної пари. Порядок смаків не береться до уваги.

Вхідні дані:

Перший рядок містить два невід'ємних цілих числа n та m — кількість
смаків та кількість несумісних пар смаків. Наступні m рядків описують
пари несумісних смаків.

Вихідні дані:

Вивести одне число — кількість способів зробити вибір.
'''
from sys import stdin


def parse(string: str) -> tuple[int, int]:
    first, second = string.split()
    return int(first), int(second)


def main():
    ice_creams, _ = parse(stdin.readline())
    count = 0
    invalids: dict[int, set] = {}

    for line in stdin.readlines():
        first, second = parse(line)

        invalids.setdefault(first, {second}).add(second)
        invalids.setdefault(second, {first}).add(first)

    for i in range(1, ice_creams + 1):
        for j in range(i+1, ice_creams+1):
            if j in invalids.get(i, {}):
                continue

            for k in range(j+1, ice_creams+1):
                if (
                    k not in invalids.get(i, {})
                    and k not in invalids.get(j, {})
                ):
                    count += 1

    print(count)


if __name__ == '__main__':
    main()
