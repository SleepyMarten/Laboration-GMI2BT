import json, requests

#function for searching after movies.
def find_movie():
    url = "http://www.omdbapi.com/?apikey=e07c004&s=" #url with api key.
    count = 0
    history_json = './data/'+'search_history.json' #file path for json file.
    while True:
        print("\nInput [Title] of the movie you are searching for.")
        movie_search = input("[Title] of Movie: ")
        try:
            respond = requests.get(url+movie_search) #requesting for all movies that match [movie_search]
            if respond.status_code == 200: #if movie exist.
                data = respond.json()   # add to json file
                for i in data['Search']:
                    count += 1
                    #print id and title of found movies.
                    print("[%s] %s"%(i['imdbID'],i['Title']))   
                    #if search result are more than 1 movie.
                if count > 1: 
                    #calling for a function to choose a movie's plot
                    find_plot() 
                    # if there is only one movie
                elif count == 1: 
                    movie_id = i['imdbID']
                    #seding imdbID to a function that outputs the plot of the movie.
                    one_find(movie_id)
            else:
                print("Code Error check the request.")
                # calling for a function to store the search history as json. ( sending json file path and input for movie search to funtion.)
            store_search_history(history_json,movie_search)
            break
        except KeyError:
            print("Movie do not exist please. Try again.")

#function to find plot of a choosen movie by ID.
def find_plot():
    url = "http://www.omdbapi.com/?apikey=e07c004&plot=full&i="
    plot_data = []
    while True:
        #note that the id can be found inside the []
        print("\nInput [ID] of a movie to view its plot.")
        print("**Note that inside the [] above are IDs for the movies**")
        movie_id = input("Input the movies [ID]: ")
        try:
            #sending a request for plot of the desired movie.
            plot_respond = requests.get(url+movie_id)
            if plot_respond.status_code == 200:
                plot_data.append(plot_respond.json())
                for i in plot_data:
                    print("\nMovie Plot:\n%s"%(i['Plot']))
                print("----------------------------------------")
                #calling for a function to store movie title and plot (sending movie title and plot to the function)
                movie_title = i['Title']
                movie_plot = i['Plot']
                store_movie(movie_title,movie_plot)
            input("Press Enter to continue.")
            break
        except KeyError:
            print("Plot not found.")
            break
        except ValueError:
            print("Please choose from t he id above.")

#if the result of find_movie = 1
def one_find(movie_id):
    plot_data = []
    url = "http://www.omdbapi.com/?apikey=e07c004&plot=full&i="
    plot_respond = requests.get(url+movie_id)
    if plot_respond.status_code == 200:
        plot_data.append(plot_respond.json())
        for i in plot_data:
            print("\n Movie Plot:\n%s"%(i['Plot']))
        print("----------------------------------------")
        movie_title = i['Title']
        movie_plot = i['Plot']
        store_movie(movie_title,movie_plot)
    input("Press Enter to continue.")

#saving search history as json file.        
def store_search_history(history_json,movie_search):
    try:
        with open(history_json,encoding='utf-8') as f:
            data = json.load(f)
            data.append(movie_search)
        with open(history_json,'w',encoding='utf-8') as f:
            json.dump(data,f , indent= 4, ensure_ascii=False)
    except FileNotFoundError:
        print("Json file not found, make sure there is a json file for store_search_history")

#saving movie title and plot as a list in a json file( Will be used to show to user.)
def store_movie(movie_title, movie_plot):
    #json file path.
    movie_json = './data/'+'movie.json'
    try:
        with open(movie_json,encoding='utf-8') as f:
            movie_data = json.load(f)
            data = {'Title': movie_title, 'Plot': movie_plot}
            movie_data.append(data)
        with open(movie_json,'w',encoding='utf-8') as f:
            json.dump(movie_data,f , indent= 4, ensure_ascii=False)
    except FileNotFoundError:
        print("Json file not found, make sure there is a json file for store_movie")

#show search history from json file that was saved from funtion store_search_history()
def show_history():
    history_json = './data/'+'search_history.json'
    try:
        with open(history_json,'r',encoding='utf-8') as f:
            data = json.load(f)
            #printing out the last 5 added to the list ( in this case those are the newest added.)
            print(data[-5:])
        input("Press Enter to return to menu")
    except FileNotFoundError:
        print("Json file not found, make sure there is a json file for show_history")

#show plot and movie that the user have been looking at.
def show_store_movie():
    movie_json = './data/'+'movie.json'
    counter = -1
    while True:
        try:
            with open(movie_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for i in data:
                    counter += 1
                    print("[%s] %s"%(counter,i['Title']))
                print("Choose a movie by number to see its plot.")
                user_input = int(input("Choose a number: "))
                print(data[user_input])
            input("Press Enter to return to menu")
            break
        except ValueError:
            print("value error")
        except FileNotFoundError:
            print("Make sure that there exist a json file for show_store_movie!")
            break
        except IndexError:
            print("Choose from the options")