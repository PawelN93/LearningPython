# 5. Napisz program, który wyświetli wszystkie liczby pierwsze od 1 do 100

from math import sqrt

for number in range(2, 101):
    isPrime = True
    for divider in range(2, int(sqrt(number))+1):
        if number % divider == 0:
            isPrime = False
            break
    if isPrime:
        print(number)