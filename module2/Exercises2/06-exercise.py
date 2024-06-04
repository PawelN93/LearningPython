# 6. Stwórz słownik, który będzie przechowywał informacje
# o krajach i ich stolicach. Dodaj do niego 5 elementów.
# Wyśwuetl dane ze słownika w formacie kraj - stolica, np.
# Polska - Warszawa

countries_capitals = {
    'Poland': 'Warsaw',
    'France': 'Paris',
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}

for country, capital in countries_capitals.items():
    print(f"{country} - {capital}")
    