# functions go here


def not_blank(question):
    valid = False

    while not valid:
        response = input("What is your name? ")

        if response != "":
            return response
        else:
            print("This cannot be blank!")


# main routine goes here
name = not_blank("Name: ")
