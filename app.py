import requests
def getPoke(Games):
    response = requests.get(f"https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15{Games.lower()}")
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
print(pokemon)

'''import requests
def getGames(Games):
    response = requests.get(f"https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15{Games.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "title": data["title"],
        "normalPrice": data["normalPrice"]
    }

game = getGames("Minecraft")
print(game)'''