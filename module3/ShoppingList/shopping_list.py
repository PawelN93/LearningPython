def read_list_from_file():
    try:
        with open("shopping_list.txt", "r") as file:
            temp_list = file.readlines()
            for index, element in enumerate(temp_list):
                temp_list[index] = element.removesuffix('\n')
            return temp_list
    except FileNotFoundError:
        return []


def write_list_to_file(shopping_list_to_write):
    with open("shopping_list.txt", "w") as file:
        for element in shopping_list_to_write:
            file.write(element+'\n')


shopping_list = read_list_from_file()
choice = None

while choice != '4':
    choice = input("What to do?\n"
                   "1 - Display shopping list\n"
                   "2 - Add new item\n"
                   "3 - Remove an item\n"
                   "4 - End\n"
                   "Choice is: ")
    match choice:
        case '1':
            if len(shopping_list) == 0:
                print("\nThe shopping list is empty\n")
            else:
                print("\nThe shopping list:")
                for index, element in enumerate(shopping_list):
                    print(f"{index + 1}. {element}")
                print()
        case '2':
            product = input("Enter the product to buy: ")
            product = product.lower().strip()
            if product not in shopping_list:
                shopping_list.append(product)
                print("\nAdded\n")
            else:
                print("\nThe product already exists\n")
        case '3':
            product = input("Enter the product to remove: ")
            product = product.lower().strip()
            if product in shopping_list:
                shopping_list.remove(product)
                print("\nRemoved\n")
            else:
                print("\nThe product doesn't exist\n")
        case '4':
            print("\nSaving file and ending the program\n")
            write_list_to_file(shopping_list)
        case _:
            print("\nUnknown command!\n")
