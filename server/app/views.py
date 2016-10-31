# -*- coding: utf-8 ?
from app import app
from flask import render_template, request
from app import base


@app.route("/")
def index():
    return render_template("index.jade")

@app.route("/users")
def users():
    return render_template("users.jade", users = base.users_list())

@app.route("/user/<int:user_id>")
def user(user_id):
    return render_template("user.jade", user = base.user_info(user_id), 
                           visit_list = base.user_visits(user_id),
                           date = "2016-10-31")

@app.route("/rooms")
def rooms():
    return render_template("rooms.jade", rooms = base.rooms_list())

@app.route("/rooms/<int:room_id>")
def room(room_id):
    return render_template("room.jade", room = base.room_info(room_id),
                           visit_list = base.room_visits(room_id),
                           date = "2016-10-31")


@app.route("/new_visit", methods = ["POST"])
def new_visit():
    rfid_id = request.form.get("rfid_id")
    room_id = request.form.get("room_id")
        
    if rfid_id is None or room_id is None:
        return "Opps",404        
    
    req = base.new_visit(rfid_id, room_id)
    app.logger.info(req)
    
    return "Ok",200