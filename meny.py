import json
from modules import find_movie, show_history, show_store_movie
url = "http://www.omdbapi.com/?apikey=e07c004&s="

while True:
    #Print out choises
    print("\n---------------------MENU---------------------")
    print("Choose a function\n")
    print("(1) Search for a movie.")
    print("(2) Show search history.")
    print("(3) Show information of movies you have selected.")
    print("(q) Exit program.")
    print("----------------------------------------------\n")
    
    inputed = input("Choose a function: ")
    if inputed == '1':
        #Call find_movie.
        find_movie()
    elif inputed == '2':
        print("Showing a list of [5] latest searches: ")
        #Call for the latest search.
        show_history()
    elif inputed == '3':
        print("Showing a list of selected movies: ")
        show_store_movie()
    elif inputed == 'q':
        print("Du har valt att avsluta programmet.")
        input("Tryck ENTER för att avsluta programmet.")
        print("Programmet avslutas.......")
        break
    else:
        print("Välj från de valet som finns i menyn!")