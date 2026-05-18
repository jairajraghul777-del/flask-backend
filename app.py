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

    username = data.get("username")
    password = data.get("password")

    query = """
    INSERT INTO users (name, password)
    VALUES (%s, %s)
    """

    cursor.execute(query, (username, password))
    conn
  
    if __name__ == "__main__":
     app.run(host="0.0.0.0", port=10000)
  
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="aws-1-ap-northeast-1.pooler.supabase.com",
    port="6543",
    database="postgres",
    user="postgres.mymlxkrilepfnxsokctn",
    password="1000billion@yjm3",
    sslmode="require"
)

cursor = conn.cursor()


@app.route('/add-card', methods=['POST'])
def add_card():
    data = request.json

    name = data.get('name')
    bio = data.get('bio')
    skills = data.get('skills')
    image_url = data.get('image_url')

    cursor.execute("""
        INSERT INTO id_cards
        (name, bio, skills, image_url)
        VALUES (%s, %s, %s, %s)
    """, (name, bio, skills, image_url))

    conn.commit()

    return jsonify({"message": "Card saved"})


@app.route('/')
def home():
    return "Server Running"


if __name__ == '__main__':
    app.run(debug=True)








