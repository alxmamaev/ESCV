# -*- coding: utf-8 ?
from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.jade")

@app.route("/people")
def people():
    return render_template("people.jade")

@app.route("/rooms")
def rooms():
    return render_template("rooms.jade")