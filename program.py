from modules import find_movie, show_history, show_store_movie

class Program():
    
    def menu(self):
        while True:
            #Print out choises
            print("\n---------------------MENU---------------------")
            print("Choose a function\n")
            print("[1] Search for a movie.")
            print("[2] Show search history.")
            print("[3] Show information of movies you have selected.")
            print("[q] Exit program.")
            print("----------------------------------------------\n")
            self.inputed = input("Choose a function: ")
            if self.inputed == '1':
                #Call find_movie.
                find_movie()
            elif self.inputed == '2':
                print("Showing a list of [5] latest searches: ")
                #Show latest 5 searches by the user..
                show_history()
            elif self.inputed == '3':
                print("Showing a list of selected movies: ")
                #Show and let user decide witch movie user want to see information of.
                show_store_movie()
            elif self.inputed == 'q':
                print("Closing the program..")
                input("Shuting down... press any key......")
                break
            else:
                print("Choose an option from the menu!")
        
#function for the menu.
def main():
    menu = Program()
    menu.menu()
#to start the menu
if __name__ == '__main__':
    main()
