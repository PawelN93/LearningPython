# 12. Napisz funkcję, która przyjmuje dwa zbiory i zwraca ich sumę, różnicę i część wspólną

def set_operation(set1, set2):
    set1 = set(set1)
    set2 = set(set2)

    union = set1 | set2
    difference = set1 - set2
    intersection = set1 & set2

    return union, difference, intersection


list1 = [1, 3, 7, 9, 11]
list2 = [2, 3, 5, 9, 10, 12]

results = set_operation(list1, list2)
print(list1)
print(list2)
print(f"Union: {results[0]}")
print(f"Difference: {results[1]}")
print(f"Intersection: {results[2]}")