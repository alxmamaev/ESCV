# -*- coding: utf-8 ?
from app import app
from flask import render_template, request
from app import base
import time

@app.route("/")
def index():
    return render_template("index.jade")

@app.route("/users")
def users():
    return render_template("users.jade", users = base.users_list())

@app.route("/user/<int:user_id>")
def user(user_id):
    date = request.args.get("date")    
    return render_template("user.jade", user = base.user_info(user_id), 
                           visit_list = base.user_visits(user_id, date),
                           cur_date = time.strftime("%Y-%m-%d"),
                           query_date = date)

@app.route("/rooms")
def rooms():
    return render_template("rooms.jade", rooms = base.rooms_list())

@app.route("/rooms/<int:room_id>")
def room(room_id):
    date = request.args.get("date")    
    return render_template("room.jade", room = base.room_info(room_id),
                           visit_list = base.room_visits(room_id, date),
                           cur_date = time.strftime("%Y-%m-%d"),
                           query_date = date)


@app.route("/new_visit")
def new_visit():
    if request.method == "POST":
        rfid_id = request.form.get("rfid_id")
        room_id = request.form.get("room_id")
        user_id = request.form.get("user_id")
    else:
        rfid_id = request.args.get("rfid_id")
        room_id = request.args.get("room_id")        
        user_id = request.args.get("user_id")
            
    if (rfid_id is None and user_id is None) or room_id is None:
        return "Opps",404        
 
    if rfid_id is not None: req = base.new_visit(rfid_id = rfid_id,room_id = room_id)
    else: req = base.new_visit(user_id = user_id,room_id = room_id)
    
    app.logger.info(req)
    
    return "Ok",200