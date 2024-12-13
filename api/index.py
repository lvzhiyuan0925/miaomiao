from flask import Flask, render_template_string, render_template, request
import os
import requests

os.chdir("/var/task/")


app = Flask(__name__, template_folder='api/htmls/')

@app.route('/')
def home():
    return render_template("/var/task/api/htmls/index.html")

@app.route('/cd')
def cd():
    param1 = request.args.get('dir')
    return os.listdir(param1)
