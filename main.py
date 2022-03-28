from flask import render_template, request
import requests, json
from __init__ import app
# create a Flask instance


# connects default URL to render .html files

@app.route('/')
def datastructuresproject():
    return render_template("datastructuresproject.html")

@app.route('/')
def navigation():
    return render_template("navigation.html")

if __name__ == "__main__":
    app.run(debug=True)