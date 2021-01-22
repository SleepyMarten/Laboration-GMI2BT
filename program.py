#LAB_1

from modules import guess_function, heltal #imported from modules.py

while True:
    #Print menu
    print("\n---------------------MENU---------------------")
    print("Choose a function to use\n")
    print("(1) Heltal function.")
    print("(2) Guess the number function.")
    print("(3) Exit.")
    print("----------------------------------------------\n")

    inputed = input("Choose a function: ")
    if inputed == '1': #starting the first function ( heltal )
        print("Welcome to the heltal function.")
        print("You need to input (2) numbers to continue.")
        while True:
            try:
                input1 = int(input("Input 1st number: ")) #user input of the 1st number
                input2 = int(input("Input 2nd number: ")) #user input of the 2nd number
                print("You have inputed: %s and %s" %(input1, input2)) #showing what number the user inputed.
                print("output: ")
                print(heltal(input1, input2)) #output of which integers are divideable
                input("Press any key to continue.")
                break
            except ValueError:
                print("Try again.")
    elif inputed == '2':
        guess_function()
    elif inputed == '3': #Exiting the program
        print("Shuting down program.")
        input("Press any key to continue.")
        break
    else:
        print("Try again.")
