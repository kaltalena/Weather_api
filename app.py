from flask import Flask, request, make_response, redirect, render_template, jsonify
import requests
import os

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/cookie/')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/bad/')
def bad():
    return '<h1>Bad Request</h1>', 400


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/change')
def change():
    return redirect('http://google.com')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/weather", methods=["GET"])
def weather():
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=15d8c47cf0c5cc8bf88d0e1dacb58b71")
    if r.status_code == 200:
        return jsonify(r.text)
    else:
        return render_template('404.html'), 404


app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
port = os.getenv('PORT')

if not port:
    port = 5081

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=port)



