import requests
import json

json_file = "file.json"
url = "http://www.omdbapi.com/?apikey=e07c004&s="

search_history = []
movie_search = "batman"
search_history.append(movie_search)
respond = requests.get(url+movie_search)
data = []
data.append(respond.json())
for i in data:
    for f in i['Search']:
        print(f['Title'])
print("pick a movie: Batman Forever")
movie_id = 'tt0112462'
plot_request  = requests.get("http://www.omdbapi.com/?apikey=e07c004&plot=full&i="+movie_id)
plot_data = []
plot_data.append(plot_request.json())
for i in plot_data:
    print(i['Plot'])
print(search_history)

#batman id i=tt0112462
