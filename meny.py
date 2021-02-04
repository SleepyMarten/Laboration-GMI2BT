import json
from modules import find_movie
url = "http://www.omdbapi.com/?apikey=e07c004&s="

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
        find_movie(url)
    elif inputed == '2':
        print("Du har valt att se dem sensate sökningarna.")
        #Call for the latest search.
    elif inputed == 'q':
        print("Du har valt att avsluta programmet.")
        input("Tryck ENTER för att avsluta programmet.")
        print("Programmet avslutas.......")
    else:
        print("Välj från de valet som finns i menyn!")