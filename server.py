from flask import Flask, render_template, url_for
from string import Template

app = Flask(__name__)

@app.route('/')
def homepage():
    return(render_template("index.html"))

@app.route('/next')
def next():
    return(render_template("diningphils.html"))

if __name__ == '__main__':
    app.run(use_reloader=True)
