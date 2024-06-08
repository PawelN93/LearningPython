# 5. Napisz funkcję is_palindrome(s), która przyjmuje
# tekst i zwraca True jeśli jest palindromem i False jeśli tekst nie jest palindromem.

def is_palindrome(s):
    s = str(s).strip().replace(" ", "")
    return s[::-1] == s


print(is_palindrome("kajak"))
print(is_palindrome("kajak kajak"))
print(is_palindrome("pies"))
