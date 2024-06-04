# 8. Stwórz program, który poprosi użytkownika o wpisanie
# tekstu w konsoli, a następnie utwórz słownik, w którym
# kluczami będą słowa występujące w tym tekście, a wartościami
# liczby wystąpień każdego słowa. Wyświetl zawartość słownika

text = input("Enter text: ")
words = text.split()
print(words)

count_words = {}

# for word in words:
#     if word in count_words.keys():
#         count_words[word] += 1
#     else:
#         count_words[word] = 1

for word in words:
    count_words[word] = count_words.get(word, 0) + 1

print(count_words)
