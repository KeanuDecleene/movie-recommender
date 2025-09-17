import tkinter as tk
from tkinter import messagebox

# Dummy recommender (replace with your ML later)
def get_recommendations(movie_name):
    recommendations = {
        "Inception": ["Interstellar", "The Matrix", "Tenet"],
        "The Matrix": ["Inception", "Blade Runner", "Ghost in the Shell"],
        "Titanic": ["The Notebook", "Romeo + Juliet", "La La Land"]
    }
    return recommendations.get(movie_name, ["No recommendations found."])

# Function for button click
def recommend():
    movie = entry.get().strip()
    results = get_recommendations(movie)

    # Clear old results
    listbox.delete(0, tk.END)

    for r in results:
        listbox.insert(tk.END, r)

# Main window
root = tk.Tk()
root.title("Movie Recommender")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter a movie that you want recommendations based off:")
label.pack(pady=5)

# Text entry
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Recommend button
button = tk.Button(root, text="Get Recommendations", command=recommend)
button.pack(pady=5)

# Listbox to show results
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Run the app
root.mainloop()
