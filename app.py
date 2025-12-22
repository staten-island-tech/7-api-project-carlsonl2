

import requests
def getGames(Games):
    response = requests.get(f"https://www.cheapshark.com/api/1.0/games?title={Games.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
        
    data = response.json()
    list = {}
    
    for i in data:
        list.append(i["external"])
        list.append(i["cheapest"])
    print(list)
        
print("Welcome to steam")
Which = input("What game are you looking for?")    
getGames(Which)





'''import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
print(pokemon)'''