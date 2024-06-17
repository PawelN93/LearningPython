import csv
import sys

fieldnames = ['Name', 'Author', 'Year']


def init_movie_lib():
    try:
        with open('movies_lib.csv') as file:
            pass
    except FileNotFoundError:
        with open('movies_lib.csv', "w", newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()


def display_movies():
    with open('movies_lib.csv', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(f"Name: {row[fieldnames[0]]}, Author: {row[fieldnames[1]]}, Year: {row[fieldnames[2]]}")


def add_movie():
    movie = input("Type name: ")
    author = input("Type author: ")
    year = input("Type year: ")

    with open('movies_lib.csv', "a", newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writerow({
            fieldnames[0]: movie,
            fieldnames[1]: author,
            fieldnames[2]: year

        })


def get_movies_list():
    movies_list = []
    with open('movies_lib.csv', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movies_list.append(row)
    return movies_list


def save_movie_list(movies_list):
    with open('movies_lib.csv', "w", newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in movies_list:
            csv_writer.writerow({
                fieldnames[0]: row[fieldnames[0]],
                fieldnames[1]: row[fieldnames[1]],
                fieldnames[2]: row[fieldnames[2]]
            })


def edit_movie():
    movie_to_edit = input("Enter the name of movie to edit: ")
    movies_list = get_movies_list()
    for index, movie in enumerate(movies_list):
        if movie[fieldnames[0]] == movie_to_edit:
            name_to_edit = input("Enter new name: ")
            author_to_edit = input("Enter new author: ")
            year_to_edit = input("Enter new year: ")
            movies_list[index][fieldnames[0]] = name_to_edit
            movies_list[index][fieldnames[1]] = author_to_edit
            movies_list[index][fieldnames[2]] = year_to_edit
            save_movie_list(movies_list)
            print("Movie changed")
            break


def remove_movie():
    movie_to_remove = input("Enter the name of movie to remove: ")
    movies_list = get_movies_list()

    for index, movie in enumerate(movies_list):
        if movie[fieldnames[0]] == movie_to_remove:
            del movies_list[index]
            save_movie_list(movies_list)
            print("Movie removed")
            break


def search_movie():
    movie_to_search = input("Enter the name of movie to search: ")
    found_movie = None

    movies_list = get_movies_list()
    for movie in movies_list:
        if movie[fieldnames[0]] == movie_to_search:
            found_movie = movie
            break
    if found_movie is not None:
        print(f"Name: {found_movie[fieldnames[0]]}, Author: {found_movie[fieldnames[1]]}, Year: {found_movie[fieldnames[2]]}")
    else:
        print("No movie found")


init_movie_lib()
while True:
    print("1. Display movies")
    print("2. Add movie")
    print("3. Edit movie")
    print("4. Remove movie")
    print("5. Search movie")
    print("6. End program")

    choice = input("Type your choice: ")

    match choice:
        case '1':
            display_movies()
        case '2':
            add_movie()
        case '3':
            edit_movie()
        case '4':
            remove_movie()
        case '5':
            search_movie()
        case '6':
            print("Ending")
            sys.exit(0)
        case _:
            print("Unknown command")
