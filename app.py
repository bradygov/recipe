from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://www.themealdb.com/api/json/v1/1/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['meal_name']
    # First, filter by ingredient
    response = requests.get(f"{BASE_URL}filter.php?i={query}")
    meals = response.json().get('meals', None)  # Get meals or None if not found

    if meals is None:
        meals = []  # Initialize meals as an empty list if None

    # Prepare a list of meal IDs and names with their thumbnails
    result = [{'idMeal': meal['idMeal'], 'strMeal': meal['strMeal'], 'strMealThumb': meal['strMealThumb']} for meal in meals]

    # If no meals found by ingredient, search by name
    if not result:
        response = requests.get(f"{BASE_URL}search.php?s={query}")
        meals_by_name = response.json().get('meals', None)
        
        if meals_by_name:
            result = [{'idMeal': meal['idMeal'], 'strMeal': meal['strMeal'], 'strMealThumb': meal['strMealThumb']} for meal in meals_by_name]

    return jsonify(result)

@app.route('/meal/<meal_id>', methods=['GET'])
def meal_details(meal_id):
    response = requests.get(f"{BASE_URL}lookup.php?i={meal_id}")
    return jsonify(response.json())

@app.route('/random', methods=['GET'])
def random_meal():
    response = requests.get(f"{BASE_URL}random.php")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)