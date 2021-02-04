import json, requests


def find_movie():
    url = "http://www.omdbapi.com/?apikey=e07c004&s="
    data = []
    history_data = []
    while True:
        print("\nInput [Title] of the movie you are searching for.")
        try:
            movie_search = input("[Title] of movie: ")
            print("\n")
            respond = requests.get(url+movie_search)
            if respond.status_code == 200:
                history_data.append(movie_search)
                data.append(respond.json())
                count = 0
                for i in data:
                    for f in i['Search']:
                        count += 1
                        print("[%s] %s"%(f['imdbID'],f['Title']))
                    if count > 1:
                        find_plot()
                    elif count == 1:
                        movie_id =f['imdbID']
                        one_find(movie_id)
                break
        except KeyError:
            print("Can't find movie. Try again.")

def find_plot():
    url = "http://www.omdbapi.com/?apikey=e07c004&plot=full&i="
    plot_data = []
    while True:
        try:
            print("\nInput [ID] of a movie to view its plot.\n")
            print("**Note that inside the [] above are IDs for the movies**")
            movie_id = input("Input the movies [ID]: ")
            plot_respond = requests.get(url+movie_id)
            plot_data.append(plot_respond.json())
            for i in plot_data:
                print("\n------------------ P L O T ------------------\n%s\n"%(i['Plot']))
            print("---------------------------------------------------")
            print("\nDo you want to check another movie's plot?")
            print("Input 'yes' to view more plots or input any key to exit.")
            user_input = input("Input: ".lower())
            if user_input == 'yes':
                input("Press ENTER to continue.")
            else:
                print("Exiting..")
                input("Press ENTER to continue.")
                break
        except KeyError:
            print("\nInput thh [ID] of the movie. You can find movie id in the []!\n")

#if the result of find_movie == 1:
def one_find(movie_id):
    url = "http://www.omdbapi.com/?apikey=e07c004&plot=full&i="
    plot_data = []
    plot_respond = requests.get(url+movie_id)
    plot_data.append(plot_respond.json())
    for i in plot_data:
            print("\n------------------ P L O T ------------------\n%s\n"%(i['Plot']))
    print("---------------------------------------------------")
    input("Press ENTER to return to menu.")
