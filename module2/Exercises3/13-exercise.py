# 13. Napisz funkcję, która przyjmuje dwa słowniki i zwraca listę kluczy z obu słowników.

def list_of_keys(dict1, dict2):
    result = list(dict(dict1).keys()) + list(dict(dict2).keys())
    return result


dictionary1 = {
    "Polska": "Warszwa",
    "Niemcy": "Berlin",
    "Francja": "Paryż"
}

dictionary2 = {
    "Japonia": "Tokia",
    "Korea Płd": "Seul",
    "Chiny": "Pekin"
}

print(list_of_keys(dictionary1, dictionary2))
