from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/index/<string:query>')
def process_request(query):
    
    result={
        "query" : query,
        "request" : "index page",
        "host IP" : "10.0.0.0:5000"
    }
    return jsonify(result)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3449)