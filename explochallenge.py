# The Explorer's Challenge - www.101computing.net/the-explorer-challenge

new_animal = False


def name_create():
    global new_animal  # Declare new_animal as global

    while not new_animal:
        animal1 = input("Enter animal 1: ")
        animal2 = input("Enter animal 2: ")

        name = animal1[:2] + animal2[2:7] + animal1[-4:]

        print("Suggested name: " + name.title())
        print("Number of characters: " + str(len(name)))
        print("Did you like the name? Answer YES or NO")
        answer = input().upper()  # .upper() handles yes, Yes, YES, etc.

        if answer == "YES":
            new_animal = True
            print("Welcome to the world, " + name.title())
        else:
            print("Let's try again")
    print("Name Creation complete.")


name_create()
