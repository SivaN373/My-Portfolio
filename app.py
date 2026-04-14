from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Create DB (auto)
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({"message": "All fields required"}), 400

    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO contacts (name, email, message, created_at)
        VALUES (?, ?, ?, ?)
    ''', (name, email, message, datetime.now()))

    conn.commit()
    conn.close()

    return jsonify({"message": "Message saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)