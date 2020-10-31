from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
import json


@app.route('/')
@app.route('/Home')
def index():
    return render_template('Reg.html')


@app.route('/autho')
def enter():
    return render_template('autho.html')


@app.route('/main')
def main_page():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
