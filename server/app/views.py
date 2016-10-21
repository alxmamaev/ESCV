# -*- coding: utf-8 ?
from app import app
from flask import render_template
from app import base

# Типа база данных =D
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

@app.route("/user/<int:user_id>")
def user(user_id):
    return render_template("user.jade", user = base.user_info(user_id))


@app.route("/users")
def users():
    return render_template("users.jade", users = base.users_list())

@app.route("/rooms")
def rooms():
    return render_template("rooms.jade", rooms = roomsData)

@app.route("/rooms")
@app.route("/rooms/<int:room>")
def room(room):
    return render_template("room.jade", room = roomsData[room])
