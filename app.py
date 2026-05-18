from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1000billion@yjm3",
    database="myapp"
)

cursor = db.cursor()


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    query = """
    INSERT INTO users (username, password)
    VALUES (%s, %s)
    """

    cursor.execute(query, (username, password))
    db.commit()

    return jsonify({
        "message": "Signup successful"
    })


@app.route('/')
def home():
    return "Server Running"


if __name__ == '__main__':
    app.run(debug=True)









