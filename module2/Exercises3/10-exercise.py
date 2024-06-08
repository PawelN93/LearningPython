# 10. Napisz funkcję, która przyjmuje liczbę i zwraca odpowiednią
# wiadomość w zależności od tego, czy liczba jest dodatnia, ujemna, czy zerowa.

def define_number(number):
    if number > 0:
        return f"Number is bigger than 0"
    elif number < 0:
        return f"Number is lower than 0"
    else:
        return f"Number equals 0"


print(define_number(5))
print(define_number(-5))
print(define_number(0))
