# 3. Napisz program, który zapyta użytkownika o wynik na egzaminie
# (od 0 do 100) i wyświetli odpowiednią ocenę:
# 90-100 -> 5
# 80-89 -> 4
# 70-79 -> 3
# 60 - 69 -> 2
# poniżej 60 -> 1

grade = int(input("Type your amount of points: "))

match grade:
    case grade if 90 <= grade <= 100:
        print("5")
    case grade if 80 <= grade <= 89:
        print("4")
    case grade if 70 <= grade <= 79:
        print("3")
    case grade if 60 <= grade <= 69:
        print("2")
    case _:
        print("1")

