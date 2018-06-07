from flask import Flask
from flask import json,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !"

@app.route('/data/')
def data():
    with open('data.json') as json_data:
        data_dict = json.load(json_data)
    return jsonify(data_dict)

if __name__ == '__main__':
    app.run(debug=True)