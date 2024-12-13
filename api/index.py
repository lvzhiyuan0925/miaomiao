from flask import Flask, render_template_string, render_template
import os
import requests

app = Flask(__name__, template_folder='api/htmls/')
os.chdir("/var/task/")

@app.route('/')
def home():
    return render_template("api/htmls/index.html")

@app.route('/about')
def about():
    return 'About'
