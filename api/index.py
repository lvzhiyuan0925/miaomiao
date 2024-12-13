from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    print(os.listdir("htmls/"))
    return render_template("htmls/index.html")  # 不要使用../html/....

@app.route('/about')
def about():
    return 'About'
