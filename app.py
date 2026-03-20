from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
 return "Home Page"


@app.route('/login')
def login():
 return "<h2>Login Page</h2>"

@app.route('/register')
def register():
 return "<h2>Register Page</h2>"
