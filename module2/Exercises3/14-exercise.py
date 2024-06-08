# 14. Napisz funkcję, która przyjmuje listę liczb i zwraca: największą liczbę, najmniejszą liczbę oraz sumę liczb.

def analyze_list(analyzed_list):
    return max(analyzed_list), min(analyzed_list), sum(analyzed_list)


list_to_analyze = [5, 10, 2, -5, 17, 27, 12]

results = analyze_list(list_to_analyze)
print(list_to_analyze)
print(f"Max: {results[0]}")
print(f"Min: {results[1]}")
print(f"Sum: {results[2]}")