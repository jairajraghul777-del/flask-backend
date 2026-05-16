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


@app.route('/signup', methods=['POST'])
def signup():

    data = request.json

    name = data.get("name")
    password = data.get("password")

    try:
        sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
        values = (name, password)

        cursor.execute(sql, values)
        db.commit()

        return jsonify({
            "success": True,
            "message": "User created"
        })

    except:
        return jsonify({
            "success": False,
            "message": "Password already exists"
        })


if __name__ == '__main__':
    app.run(debug=True)
 
print("Server started")
print(db)
 
 
 
 
 
 
 
 
 
 
 
 
 
 

  
  
 