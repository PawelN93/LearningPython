# 17. Napisz funkcję, która przyjmuje listę liczb od
# użytkownika, a następnie zwraca te liczby, które występują na liście więcej niż raz.

def repeated_nums(numbers):
    repeats = []
    numbers = list(numbers)
    for number in numbers:
        if number not in repeats and numbers.count(number) > 1:
            repeats.append(number)
    return repeats


numbers = [
    2, 5, 3, 2, 6, 6, 7, 4, 3, 10, 11, 1, 2, 3, 5, 7, 8, 10, 17, 23, 3
]

print(repeated_nums(numbers))