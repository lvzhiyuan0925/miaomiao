from flask import Flask, render_template_string, render_template, request
import os
import requests

os.chdir('/var/task/api/')

app = Flask(__name__, template_folder='/var/task/api/htmls/')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cd')
def cd():
    param1 = request.args.get('dir')
    return os.listdir(param1)

@app.route('/<filename>')
def serve_file(filename):
    return send_from_directory('htmls', filename)
