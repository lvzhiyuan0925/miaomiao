from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    print(os.listdir("api/htmls/"))
    return render_template("api/htmls/"+os.listdir("api/htmls/")[0])

@app.route('/about')
def about():
    return 'About'
