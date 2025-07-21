from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)


def get_user_name():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            database=os.environ.get("DB_NAME", "testdb"),
            user=os.environ.get("DB_USER", "testuser"),
            password=os.environ.get("DB_PASS", "testpass"),
        )
        cur = conn.cursor()
        cur.execute("SELECT name FROM users LIMIT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            return {"username": result[0], "error": None}
        return {"username": "No user found", "error": None}
    except Exception as e:
        return {"username": None, "error": str(e)}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/user")
def api_user():
    user_data = get_user_name()
    return jsonify(user_data)


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
