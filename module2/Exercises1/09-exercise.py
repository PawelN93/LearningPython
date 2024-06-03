# 9. Pobierz od użytkownia 3 liczby całkowite i uporządkuj je w kolejności
# od najmniejszej do największej

a = int(input("Give first number: "))
b = int(input("Give second number: "))
c = int(input("Give third number: "))

if a > b and a > c:
    if b > c:
        print(f"{c} - {b} - {a}")
    else:
        print(f"{b} - {c} - {a}")
elif b > a and b > c:
    if a > c:
        print(f"{c} - {a} - {b}")
    else:
        print(f"{a} - {c} - {b}")
else:
    if a > b:
        print(f"{b} - {a} - {c}")
    else:
        print(f"{a} - {b} - {c}")
