import json

# Funktion zum Anpassen der Rezeptmengen basierend auf der Anzahl der Personen
def adjust_recipe(recipe, num_people):
    factor = num_people / recipe["servings"]
    adjusted_ingredients = {
        ingredient: int(amount * factor)  # int() für ganze Zahlen bei den Mengen
        for ingredient, amount in recipe["ingredients"].items()
    }
    # Rückgabe eines neuen, angepassten Rezepts mit der aktualisierten Portionenzahl
    return {
        "title": recipe["title"],
        "ingredients": adjusted_ingredients,
        "servings": num_people
    }

# Funktion zum Laden des Rezepts aus einem JSON-String
def load_recipe(json_string):
    return json.loads(json_string)

# Hauptbereich des Programms
if __name__ == '__main__':
    # Beispiel JSON für ein Rezept
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    # Rezept laden
    recipe = load_recipe(recipe_json)
    # Rezept anpassen
    adjusted_recipe = adjust_recipe(recipe, 2)
    print("Angepasstes Rezept:", adjusted_recipe)
