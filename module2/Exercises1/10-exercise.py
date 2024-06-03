# 10. Stwórz grę, w której wylosujesz liczbę z przedziału
# 1-100, zapiszesz tę liczbę do zmiennej, a następnie poprosisz
# użytkownika o odgadniecie tej liczby.

import random

random_number = random.randint(1, 100)

given_number = None
tries = 1

while random_number != given_number:
    given_number = int(input("Give the number: "))
    if given_number == random_number:
        print("You win!")
        break
    elif given_number > random_number:
        print("Given number is too big")
    else:
        print("Given number is too low")
    tries += 1
print("Tries: " + str(tries))