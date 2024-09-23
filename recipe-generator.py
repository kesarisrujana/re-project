import tkinter as tk
from tkinter import scrolledtext
import cohere

# Replace 'your-api-key' with your actual Cohere API key
cohere_api_key = 'our-api-key********'
co = cohere.Client(cohere_api_key)

def generate_recipe():
    meal_type = meal_type_entry.get()
    cuisine_type = cuisine_type_entry.get()
    time = time_entry.get()
    ingredients = ingredients_entry.get()

    prompt = (
        f"Create a recipe for a {meal_type} meal. "
        f"Cuisine type: {cuisine_type}. "
        f"Time to prepare: {time}. "
        f"Ingredients: {ingredients}."
    )

    try:
        response = co.chat(
            model='command-light-nightly',
            message=prompt,
            max_tokens=500
        )
        recipe = response.text.strip()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, recipe)
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}")

root = tk.Tk()
root.title("Recipe Generator")

tk.Label(root, text="Meal Type:").pack()
meal_type_entry = tk.Entry(root, width=50)
meal_type_entry.pack()

tk.Label(root, text="Cuisine Type:").pack()
cuisine_type_entry = tk.Entry(root, width=50)
cuisine_type_entry.pack()

tk.Label(root, text="Time (e.g., 30 minutes):").pack()
time_entry = tk.Entry(root, width=50)
time_entry.pack()

tk.Label(root, text="Ingredients (comma separated):").pack()
ingredients_entry = tk.Entry(root, width=50)
ingredients_entry.pack()

generate_button = tk.Button(root, text="Generate Recipe", command=generate_recipe)
generate_button.pack()

tk.Label(root, text="Generated Recipe:").pack()
result_text = scrolledtext.ScrolledText(root, width=60, height=20)
result_text.pack()

root.mainloop()
