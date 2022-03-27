from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
def print_hello():
    return jsonify("Hello")
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)