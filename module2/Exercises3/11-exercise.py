# 11. Napisz funkcję, która przyjmuje
# numer dnia tygodnia i zwraca nazwę tego dnia, używając instrukcji match case.

def check_day(number_of_day):
    match int(number_of_day):
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Unknown"


print(check_day(2))
print(check_day(5))
print(check_day(7))
print(check_day(0))
