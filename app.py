from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # database connection
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # create table
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

        # insert data
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')