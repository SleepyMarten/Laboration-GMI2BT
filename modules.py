from random import randint

#Input 2 numbers and it will find number from 0-1000 that is divideable Integers.
def heltal(input1, input2):
    numbers = []
    for num in range(1, 1001):
        if(num/input1).is_integer() & (num/input2).is_integer():
            numbers.append(num)
    return numbers

#randomizing a number from 1 to 100 for the user to guess.
def guess_function():
    rnd = randint(1, 101)
    print("\nHINT (do not look): %s\n" % (rnd)) #using this to confirm what number the rnd has randomized.
    print("Welcome to the guess the number funtion.")
    print("You will have to guess a number bewteen number 1 and 100.\n")
    while (True):
        user_input = input('Input the number you think is right: ')
        try:
            user_answer = int(user_input)
            if user_answer == rnd:
                print("\nCongratulation! You guessed right!\n")
                input("Press any key to continue.")
                break
            elif user_answer < rnd:
                print("WRONG! You guessed to LOW, try to guess HIGHER.\n")
            else:
                print("WRONG! You guessed to HIGH, try to guess LOWER.\n")
        except ValueError:
            print("Wrong input. Try again.\n")
