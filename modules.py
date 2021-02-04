import json
import requests

def find_movie(url):
    data = []
    plot_data = []
    print("Input NAME/TITLE of movie.")
    movie_search = ''
    while not movie_search:
        movie_search = input("NAME/TITLE of movie: ")
    respond  = requests.get(url+movie_search)
    data.append(respond.json())
    counter = -1
    for i in data:
        for f in i['Search']:
            counter += 1
            print("[%s] %s"%(counter,f['Title']))
    print("Please select a movie, you can select a movie by its [number].")
    for i in data:
        for f in i['Search']:
            f['imdbID']