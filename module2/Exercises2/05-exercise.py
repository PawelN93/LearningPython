# 5. Korzystajac z list z poprzedniego ćwiczenia, wyświetl
# tylko te imiona, które są obecne w pierwszej liście

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

print(set(names1) - set(names2))