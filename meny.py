import json
from modules import find_movie

while True:
    #Print out the menu
    print("\n---------------------MENU---------------------")
    print("Choose a function\n")
    print("(1) Search for a movie.")
    print("(2) Show search history.")
    print("(q) Exit program.")
    print("----------------------------------------------\n")
    
    inputed = input("Choose a function: ")
    if inputed == '1':
        #Call find_movie.
        find_movie()
    elif inputed == '2':
        print("Showing Search history.")
        #Call for the latest search.
        input("Press ENTER to continue.")
    elif inputed == 'q':
        print("You have chosen to exit the program.")
        input("Press ENTER to continue")
        print("Shuting down program.......")
        break
    else:
        print("Choose a option from the menu!")
        input("Press ENTER to continue")