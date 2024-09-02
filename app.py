from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://www.themealdb.com/api/json/v1/1/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    meal_name = request.form['meal_name']
    response = requests.get(f"{BASE_URL}search.php?s={meal_name}")
    return jsonify(response.json())

@app.route('/random', methods=['GET'])
def random_meal():
    response = requests.get(f"{BASE_URL}random.php")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)