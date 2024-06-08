# 15. Napisz funkcję, która przyjmuje listę imion i wypisuje je w odwrotnej kolejności, używając pętli.

def reverse_list(names):
    for index in range(len(names)-1, -1, -1):
        print(names[index])


names = ["Paweł", "Magda", "Piotr", "Agata"]
reverse_list(names)