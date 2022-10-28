from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/details', methods=['GET'])
def get_details():
    if request.method == 'GET':
        return jsonify({"slackUsername": 'Keke',
                        "backend": True,
                        "age": 23,
                        "bio": 'Software Engineer with '
                               'focus on Back-End Web development and Android using Android and Java'})
