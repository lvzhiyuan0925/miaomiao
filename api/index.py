from flask import Flask, render_template_string
import os
import requests

app = Flask(__name__, template_folder='api/htmls/')
os.chdir()

@app.route('/var/task/api/htmls/index.html')
def home():
    return render_template_string("")

@app.route('/about')
def about():
    return 'About'
