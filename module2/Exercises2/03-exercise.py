# 3. Stwórz listę, którą wypełnisz 10 liczbami całkowitymi.
# Znajdź najmniejszą i największą lczbę.

numbers = [
    10,
    11,
    5,
    60,
    70,
    6,
    4,
    100,
    2,
    18
]

max = numbers[0]
min = numbers[0]

for number in numbers:
    if number > max:
        max = number
    if number < min:
        min = number
print(f"Min {min}")
print(f"Max {max}")