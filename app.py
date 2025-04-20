from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400

@app.route('/api/v1.0/predict')
def calc():
    num1 = request.args.get('num1', 0)
    num2 = request.args.get('num2', 0)

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({"error": "Parametry muszą być liczbami"}), 400

    if num1 + num2 > 5.8:
        pred = 1
    else:
        pred = 0
    return jsonify({"prediction": pred, "features": {"num1": num1, "num2": num2}})

if __name__ == '__main__':
    app.run()