# 8. Napisz funkcję, która przyjmuje imię i wiek, a następnie
# zwraca zdanie “Nazywam się [imię] i mam [wiek] lat.” używając f-strings.

def prepare_string_name_age(name, age):
    return f"Nazywamm się {name} i mam {age} lat."


print(prepare_string_name_age("Paweł", 30))
