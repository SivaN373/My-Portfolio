from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# -----------------------------
# DATABASE INIT
# -----------------------------
def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# ROUTES
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validation
        if not name or not email or not message:
            return jsonify({"message": "All fields are required"}), 400

        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO contacts (name, email, message, created_at)
            VALUES (?, ?, ?, ?)
        ''', (name, email, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        conn.commit()
        conn.close()

        return jsonify({"message": "Message saved successfully!"})

    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500


# -----------------------------
# RUN APP (PRODUCTION READY)
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)