
from flask import Flask, jsonify, request
from lib import scrape

app = Flask(__name__)

@app.route('/tweets/sentiment')
def sentiment():
    query = request.args.get('query')
    return jsonify(scrape.get_tone(query, 100))


if __name__ == '__main__':
    app.run(debug=True)
=======
