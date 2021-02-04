import json,requests

class Movies():
    
    def find_movie(self):
        url = "http://www.omdbapi.com/?apikey=e07c004&s="
        #self.data = []
        #self.history = []
        count = 0
        print("\nInput [Title] of the movie you are searching for.")
        try:
            self.movie_search = input("[Title] of movie: ")
            print("\n")
            respond = requests.get(url+self.movie_search)
            data = respond.json()
            if respond.status_code == 200:
                self.history = data['Search']
                for i in data['Search']:
                    print("[%s] %s"%(i['imdbID'],i['Title']))
            else:
                print("Error")
                
Movies.find_movie()