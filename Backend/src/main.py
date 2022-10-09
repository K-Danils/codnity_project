from app import app, ar
from flask import jsonify

# contains all endpoints for the backend
@app.route("/get-articles", methods=["GET"])
def get_articles():
    return  jsonify(ar.get_articles())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)