from flask import Flask, render_template_string, render_template, request
import os
import requests


app = Flask(__name__, template_folder='/var/task/api/htmls/')

@app.route('/')
def home():
    return render_template("index.html")
