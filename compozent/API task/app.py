from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

foods = [
    {"id": 1, "name": "Pizza", "category": "Italian", "rating": 4.5},
    {"id": 2, "name": "Sushi", "category": "Japanese", "rating": 4.7},
    {"id": 3, "name": "Burger", "category": "American", "rating": 4.3},
    {"id": 4, "name": "Tacos", "category": "Mexican", "rating": 4.6},
    {"id": 5, "name": "Pasta", "category": "Italian", "rating": 4.8},
    {"id": 6, "name": "Ramen", "category": "Japanese", "rating": 4.6},
    {"id": 7, "name": "Burrito", "category": "Mexican", "rating": 4.4},
    {"id": 8, "name": "Fried Chicken", "category": "American", "rating": 4.2},
    {"id": 9, "name": "Peking Duck", "category": "Chinese", "rating": 4.9},
    {"id": 10, "name": "Paella", "category": "Spanish", "rating": 4.7}
]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)

@app.route('/api/foods', methods=['POST'])
def add_food():
    new_food = request.get_json()
    new_food["id"] = len(foods) + 1  
    foods.append(new_food)
    return jsonify(new_food), 201  

@app.route('/api/foods/<int:id>', methods=['PUT'])
def update_food(id):
    updated_food = request.get_json()
    for food in foods:
        if food['id'] == id:
            food['name'] = updated_food.get('name', food['name'])
            food['category'] = updated_food.get('category', food['category'])
            food['rating'] = updated_food.get('rating', food['rating'])
            return jsonify(food)
    return jsonify({"error": "Food item not found"}), 404

@app.route('/api/foods/<int:id>', methods=['DELETE'])
def delete_food(id):
    global foods
    foods = [food for food in foods if food['id'] != id]
    return jsonify({"message": f"Food item {id} deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
