# 8. Napisz program, który sprawdzi czy podane imię
# jest imieniem męskim czy żeńskim (załóż, że imiona żeńskie kończą się na a)

name = input("Give the name: ")

if name.endswith("a"):
    print("The name is for girl")
else:
    print("The name is for boy")