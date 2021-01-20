import modules

# Calling the functions
start = True
while(start):
    modules.menu()
    user_input = input("Input: ")
    try:
        inputed = int(user_input)
        if inputed == 1:
            modules.heltal()
        elif inputed == 2:
            modules.guess_function()
        elif inputed == 3:
            print("The program is shuting down.....")
            modules.press()
            start = False
        else:
            print("Try again menu try")
    except ValueError:
        print("Input a number (1) (2) or (3)")
        modules.press()
