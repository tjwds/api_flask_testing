from flask import Flask, jsonify

app = Flask(__name__)

groceries = { "fruit": ["bananas", "pears", {"apples": ["granny smith",
    "macintosh", "gala"]}], "personal care": ["toothpaste", "chapstick"]}

@app.route('/')
def hey_world():
    return jsonify(id=groceries)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
