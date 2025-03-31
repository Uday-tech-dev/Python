from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

db_path = "uday_hospitals.db"

# Initialize database
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            height INTEGER,
            weight INTEGER,
            package TEXT,
            payment_method TEXT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    height = request.form['height']
    weight = request.form['weight']
    package = request.form['package']
    payment_method = request.form['payment_method']
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO transactions (name, age, height, weight, package, payment_method) 
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (name, age, height, weight, package, payment_method))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
