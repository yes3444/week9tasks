from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

app.route('/animals', methods=['GET'])
def get_animals():
    animals = ["Cat", "Dog", "Bird", "Fish", "Elephant", "Lion"]
    return jsonify(animals)

@app.route('/studentInfo', methods=['POST'])
def get_studentProfile():
    data = request.get_json()
    print(f"Received data: {data}")
    name = request.json.get("name")
    print(f"Received data: {name}")
    if name == "Tom":
        student = {
        "name": name,
        "age": 22,
        "course": "COM4103 Software Development",
        "level" : "Level 4",
        "department" : "Computer Science",
        "photo":"https://m.media-amazon.com/images/S/pv-target-images/057c3ca9c30e7f315944d9f169fc4bab4e72379346e9e0a88f7d10c0568d2622.jpg"
        }
    elif name == "Lucy":
        student = {
        "name": name,
        "age": 23,
        "course": "COM5103 Software Engineering",
        "level" : "Level 5",
        "department" : "Computer Science",
        "photo":"https://charatoon.com/photo/13359.png"
        }
    else:
        student = {
        "name": name,
        "age": 21,
        "course": "COM3013 Web Technologies",
        "level" : "Level 3",
        "department" : "Computer Science",
        "photo":"https://media.newyorker.com/photos/59095bb86552fa0be682d9d0/master/pass/Monkey-Selfie.jpg"
        }
    return jsonify(student)

