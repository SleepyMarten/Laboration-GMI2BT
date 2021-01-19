def menu():
    print("\n---------------------MENU---------------------")
    print("Choose a function to use\n")
    print("(1) Heltal function.")
    print("(2) Guess the number function.")
    print("(3) Exit.")
    print("----------------------------------------------\n")


def choose_function():
    start = True
    while(start):
        menu()
        user_input = input("Input: ")
        try:
            inputed = int(user_input)
            if inputed == 1:
                heltal()
            elif inputed == 2:
                guess_function()
            elif inputed == 3:
                print("The program is shuting down.....")
                press()
                start = False
            else:
                print("Try again menu try")
        except ValueError:
            print("Input a number (1) (2) or (3)")
            press() 


def press():
    input("\nPress any key to continue\n")


def heltal():
    numbers = []
    number_list = []
    for num in range(0, 1001):
        number_list.append(num)
    print("Welcome to the heltal function.")
    print("Input 2 numbers to run the function.")
    while (True):
        first_input = input("\nInput 1st number: ")
        second_input = input("Input 2nd number: ")
        try:
            first = int(first_input)
            second = int(second_input)
            for num in number_list:
                if(num/first).is_integer() & (num/second).is_integer():
                    numbers.append(num)
            print("\nThe inputed numbers were: %s and %s." % (first, second))
            print("ANSWER %s: " % (numbers))
            press()
            break
        except ValueError:
            print("Try again.")


def guess_function():
    import random
    rnd = random.randint(1, 100)
    x = int(rnd)
    print("\nHINT (do not look): %s\n" % (x))
    print("Welcome to the guess the number funtion.")
    print("You will have to guess a number bewteen number 1 and 100.\n")
    while (True):
        user_input = input('Input the number you think is right: ')
        try:
            user_answer = int(user_input)
            if user_answer == x:
                print("\nCongratulation! You guessed right!\n")
                press()
                break
            elif user_answer < x:
                print("WRONG! You guessed to LOW, try to guess HIGHER.\n")
            else:
                print("WRONG! You guessed to HIGH, try to guess LOWER.\n")
        except ValueError:
            print("Wrong input. Try again.\n")
