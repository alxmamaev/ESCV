# -*- coding: utf-8 ?
from app import app
from flask import render_template

# Типа база данных =D
peopleData = [
	{
		"id": 0,
		"img": "../static/img/nevskiy!.jpg",
		"name": "Alx Nevskiy!",
		"description": "Do you speak Engish?"
	}
]
roomsData = [
	{
		"id": 0,
		"img": "../static/img/stolovka.jpg",
		"label": "The best dining room in the world!",
		"description": "Burgers... With Pasta?!"
	}
]
# Конец типа базы данных

@app.route("/")
def index():
    return render_template("index.jade")

@app.route("/people")
def people():
    return render_template("people.jade", people = peopleData)

@app.route("/rooms")
def rooms():
    return render_template("rooms.jade", rooms = roomsData)

@app.route("/people")
@app.route("/people/<int:man>")
def man(man):
    return render_template("man.jade", man = peopleData[man])

@app.route("/rooms")
@app.route("/rooms/<int:room>")
def room(room):
    return render_template("room.jade", room = roomsData[room])
