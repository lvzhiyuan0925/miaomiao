from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='api/htmls')

@app.route('/')
def home():
    
    return render_template("index.html")

@app.route('/about')
def about():
    return 'About'
