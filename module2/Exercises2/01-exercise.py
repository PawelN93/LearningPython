# 1. Stwórz listę, którą wypełnisz 10 liczbami całkowityi i zwróć sume
# wszystkich liczb z tej listy

numbers = []

for _ in range(0, 10):
    numbers.append(int(input("Podaj liczbe: ")))
print(sum(numbers))
