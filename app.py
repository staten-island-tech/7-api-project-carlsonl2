import tkinter as tk
from tkinter import messagebox
import requests

def getGames(game_name):
    response = requests.get(
        f"https://www.cheapshark.com/api/1.0/games?title={game_name.lower()}"
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if not data:
        return None

    # Return the first result (same as your original logic)
    return {
        "title": data[0]['external'],
        "cheapest_price": data[0]['cheapest']
    }

def check_price():
    game_name = entry.get().strip()

    if not game_name:
        messagebox.showwarning("Input Error", "Please enter a game name.")
        return

    result = getGames(game_name)

    if not result:
        result_label.config(text="Game not found.")
    else:
        result_label.config(
            text=f"Title: {result['title']}\nCheapest Price: ${result['cheapest_price']}"
        )

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Game Price Checker")
root.geometry("400x200")

tk.Label(root, text="Enter Game Name:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Price", command=check_price).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()




'''import tkinter as tk
window = tk.Tk()
window.title("Game Price Checker")
window.geometry("400x200")

prompt = tk.Label(window, text="Type your message below:",
font=("Ariel", 14))

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)



window.mainloop()
import requests
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
        print(f"{key} → {value}")


def pricecheck():
    game_name = entry.get().strip()
    result = getGames(game_name)'''
