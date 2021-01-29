import csv, json, modules

#Note that I comment in English because it is easier.
#The Program UI however is in Swedish so other people in my house can test the program.

csv_file = 'labb2-personer.csv'
json_file = 'student_data.json'
while True:
    #Print out the menu
    print("\n---------------------MENU---------------------")
    print("Välj en funktion\n")
    print("(1) Visa CSV listan.")
    print("(2) Spara CSV listan som JSON fil.\n")
    print("(3) Mata in information om en student.")
    print("(4) Ta bort en student från student listan.")
    print("(5) Visa lista av studenter.\n")
    print("\n(q) AVSLUTA PROGRAMMET.")
    print("----------------------------------------------\n")
    
    inputed = input("VÄLJ EN FUNKTION: ")
    if inputed =='1': #Show the CSV list.
        print("Öppnar och visar CSV filen: \n")
        modules.read_csv(csv_file)
        
    elif inputed =='2': # saveing the CSV list as JSON file ( dict in a list).
        print("Konverterar CSV filen till JSON fil......")
        modules.save_csv(csv_file, json_file)
        
    elif inputed == '3': # Add student and student information to the student list(student_data.json)
        print("Mata in information om studenten som ska läggas in till student listan.")
        modules.add_student(json_file)
        
    elif inputed == '4': # Remove student information from the student list.
        print("Välj student som ska raders från student listan.")
        modules.remove_student(json_file)
        
    elif inputed == '5': # Showing a list of students.
        print("Visar en lista av studenter.\n")
        modules.show_student(json_file)
        
    elif inputed == 'q': # Exiting the program.
        print("Programmet avslutas.")
        input("Tryck Enter för att forstsätta.")
        break
    else:
        print("Vänligen välj en funktion ( 1-5 ) ")