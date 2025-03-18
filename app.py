from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load ingredient data
with open("subway_full_nutrition.json", "r", encoding="utf-8") as file:
    ingredients = json.load(file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_ingredients")
def get_ingredients():
    return jsonify(ingredients)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
