# 7. Posortuj słownik z poprzedniego ćwiczenia w kolejności
# alfabetycznej

countries_capitals = {
    'Poland': 'Warsaw',
    'France': 'Paris',
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}

countries = list(countries_capitals.keys())
countries.sort()


for country in countries:
    print(f"{country} - {countries_capitals.get(country)}")
