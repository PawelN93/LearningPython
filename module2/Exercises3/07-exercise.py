# 7. Napisz funkcję fibonacci(n), która przyjmuje liczbę całkowitą n i zwraca n-tą liczbę w ciągu Fibonacciego.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(19))