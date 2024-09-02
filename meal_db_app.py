import requests

# Base URL for TheMealDB API
BASE_URL = "https://www.themealdb.com/api/json/v1/1/"

def search_meal_by_name(meal_name):
    """Search for a meal by its name."""
    response = requests.get(f"{BASE_URL}search.php?s={meal_name}")
    return response.json()

def list_meals_by_first_letter(letter):
    """List all meals starting with a specific letter."""
    response = requests.get(f"{BASE_URL}search.php?f={letter}")
    return response.json()

def get_random_meal():
    """Get a random meal."""
    response = requests.get(f"{BASE_URL}random.php")
    return response.json()

def display_meal(meal):
    """Display meal details."""
    if meal:
        meal_info = meal.get("meals")[0]
        print(f"\nMeal: {meal_info['strMeal']}")
        print(f"Cuisine: {meal_info['strArea']}")
        print(f"Category: {meal_info['strCategory']}")
        print(f"Instructions: {meal_info['strInstructions']}")
        print(f"Image: {meal_info['strMealThumb']}")
        print("Ingredients:")
        for i in range(1, 21):
            ingredient = meal_info[f'strIngredient{i}']
            if ingredient:
                measure = meal_info[f'strMeasure{i}']
                print(f"- {ingredient} ({measure})")
    else:
        print("No meal found.")

def main():
    print("Welcome to the Meal DB Recipe App!")
    while True:
        print("\nChoose an option:")
        print("1. Search meal by name")
        print("2. List meals by first letter")
        print("3. Get a random meal")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            meal_name = input("Enter the meal name: ")
            meal = search_meal_by_name(meal_name)
            display_meal(meal)
        
        elif choice == '2':
            letter = input("Enter the first letter: ")
            meals = list_meals_by_first_letter(letter)
            if meals.get("meals"):
                print("\nMeals found:")
                for meal in meals["meals"]:
                    print(f"- {meal['strMeal']}")
            else:
                print("No meals found.")
        
        elif choice == '3':
            random_meal = get_random_meal()
            display_meal(random_meal)
        
        elif choice == '4':
            print("Exiting the app. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()