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


@app.route('/add')
def add_page():
    return render_template('add_page.html')


@app.route('/katalog')
def katalog_page():
    return render_template('katalog_page.html')


if __name__ == '__main__':
    app.run(debug=True)
