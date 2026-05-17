 from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="900billion@yuvraj1",
    database="myapp"
)

cursor = db.cursor()

@app.route('/')
def home():
    return "Backend Running ✔️"


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get('name')
    password = data.get('password')

    # Empty check
    if not name or not password:
        return jsonify({
            "success": False,
            "message": "Name and Password required"
        }), 400

    # Insert into table
    query = "INSERT INTO users (name, password) VALUES (%s, %s)"
    values = (name, password)

    cursor.execute(query, values)
    db.commit()

    return jsonify({
        "success": True,
        "message": "Signup Successful"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
 
 
 
 
 
 

  
  
 
