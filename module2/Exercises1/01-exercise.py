# 1. Napisz program, który sprawdza, czy podana przez użytkownika
# liczba jest parzysta czy nie parzysta

number = int(input("Type the number: "))

if number % 2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")