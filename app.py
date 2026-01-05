

'''import requests
def getGames(Games):
    response = requests.get(f"https://www.cheapshark.com/api/1.0/games?title={Games.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
        
    data = response.json()

    for i in range(len(data)):
        return {
            "title": data[i]['external'],
            "cheapest_price": data[i]['cheapest'],
            }
  
game = input("Enter Game name: ")
game = getGames(game)
if game:
    for key, value in game.items():
        print(f"{key} → {value}")'''
import tkinter as tk # bring in tkinter and call it tk
# Create the main window (like your app's frame)
window = tk.Tk()
window.title("Message Reverser") # title at the top of the window
window.geometry("400x250") # set the size (width x height)
window.resizable(False, False) # keep it from being resized





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