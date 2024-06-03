# 2. Napisz program, który sprawdza, czy podana przez użytkownika
# liczba jest większa od 0, mniejsza od 0, równa 0

number = int(input("Type the number: "))

if number > 0:
    print("Number is bigger than zero")
elif number < 0:
    print("Number is lower than zero")
else:
    print("Number equals zero")