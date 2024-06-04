# 2. Stwórz listę, która będzie zawierac 10 słów
# Następnie stwórz drugę listę, która będzie zawierać
# tylko te słowa, które mają więcej niż 5 liter

words = [
    'auto',
    'piłka',
    'książka',
    'rower',
    'ryba',
    'ser',
    'autobus',
    'kot',
    'pies',
    'dom'
]

long_words = []

for word in words:
    if len(word) >= 5:
        long_words.append(word)

print(long_words)
