from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Supabase PostgreSQL connection
conn = psycopg2.connect(
    host="aws-1-ap-northeast-1.pooler.supabase.com",
    port=6543,
    database="postgres",
    user="postgres.mymlxkrilepfnxsokctn",
    password="1000billion@yjm3",
    sslmode="require"
)

cursor = conn.cursor()


@app.route('/')
def home():
    return "Backend Running ✔️"


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get("name")
    password = data.get("password")

    query = """
    INSERT INTO users (name, password)
    VALUES (%s, %s)
    """

    cursor.execute(query, (name, password))
    conn
  
    if __name__ == "__main__":
     app.run(host="0.0.0.0", port=10000)
   
 
 
 
 

  
  
 