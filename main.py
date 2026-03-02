from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")

def json():
    marks = {
        "Sam":36,
        "Rohan":67,
        "Akash":78,
        "Shubham":100,
        "Reena":67
    }
    values =  [1, marks, 67]
    return jsonify(values)

app.run(debug=True)