# 3. Napisz funkcję factorial(n), która przyjmuje liczbę całkowitą n i zwraca jej silnię (n!).

def factorial(n):
    factorial_num = 1
    for i in range(2, n+1):
        factorial_num *= i
    return factorial_num


print(factorial(5))
