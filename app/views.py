# -*- coding: utf-8 ?
from app import app
from app import export
from app import base

import time
import  os

from flask import render_template, request, send_file

@app.route("/")
def index():
    return render_template("index.jade")

@app.route("/users")
def users():
    return render_template("users.jade", users = base.users_list())

@app.route("/users/<int:user_id>")
def user(user_id):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    cur_date = time.strftime("%Y-%m-%d")

    if start_date is None: start_date = cur_date
    if end_date is None: end_date = cur_date

    return render_template("user.jade", user = base.user_info(user_id),
                           visit_list = base.user_visits(user_id, start_date, end_date),
                           cur_date = cur_date,
                           start_date = start_date,
                           end_date = end_date)

@app.route("/users/<int:user_id>/csv")
def user_csv(user_id):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    cur_date = time.strftime("%Y-%m-%d")

    if start_date is None: start_date = cur_date
    if end_date is None: end_date = cur_date

    file_name = export.to_csv(base.user_visits(user_id, start_date, end_date))
    return send_file(file_name, attachment_filename = "test"), 200


@app.route("/rooms")
def rooms():
    return render_template("rooms.jade", rooms = base.rooms_list())

@app.route("/rooms/<int:room_id>")
def room(room_id):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    cur_date = time.strftime("%Y-%m-%d")

    if start_date is None: start_date = cur_date
    if end_date is None: end_date = cur_date

    return render_template("room.jade", room = base.room_info(room_id),
                           visit_list = base.room_visits(room_id, start_date, end_date),
                           cur_date = cur_date,
                           start_date = start_date,
                           end_date = end_date)


@app.route("/rooms/<int:room_id>/csv")
def room_csv(room_id):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    cur_date = time.strftime("%Y-%m-%d")

    if start_date is None: start_date = cur_date
    if end_date is None: end_date = cur_date

    file_name = export.to_csv(base.room_visits(room_id, start_date, end_date))
    return send_file(file_name, attachment_filename = "test"), 200


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
