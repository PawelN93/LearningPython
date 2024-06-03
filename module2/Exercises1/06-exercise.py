# 6. Napisz program, który wyświetli sumę wszystkich liczb parzystych
# z przedziału 1 - 100

sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(sum)