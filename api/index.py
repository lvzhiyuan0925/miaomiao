from flask import Flask, render_template_string
import os
import requests

app = Flask(__name__, template_folder='api/htmls/')

@app.route('/')
def home():
    return render_template_string(requests.get("https://raw.githubusercontent.com/lvzhiyuan0925/miaomiao/refs/heads/main/api/htmls/index.html").text)

@app.route('/about')
def about():
    return 'About'
