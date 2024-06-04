# 4. Stwórz 2 listy, które wypełnisz imionami - po 5 immion
# w każdej z list. Wyswietl te imiona

names1 = [
    'Paweł',
    'Piotr',
    'Adam',
    'Magda',
    'Paulina'
]

names2 = [
    'Adam',
    'Rafał',
    'Ewa',
    'Magda',
    'Paweł'
]

print(set(names1) & set(names2))
