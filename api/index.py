from flask import Flask, render_template_string, render_template, request
import os
import requests

app = Flask(__name__, template_folder='api/htmls/')
os.chdir("/var/task/")

@app.route('/')
def home():
    return render_template("/var/task/api/htmls/index.html")

@app.route('/cd')
def cd():
    param1 = request.args.get('dir')
    return os.listdir(param1)

@app.route('/write')
def write():
    try:
    with open('example.txt', 'r') as file:
        content = file.read()
    except PermissionError:
        return "权限不足"
    except Exception as e:
        return str(e)

    return "成功创建了文件"
