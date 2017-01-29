# -*- coding: utf-8 -*- ?
import config
from app import app

import time
import os
import json
import sqlite3 as sqlite

DATABASE_URL = os.environ.get("DATABASE_URL", default = "escv.db")
USER_IMAGES_PATH = "../static/img/users/user_%s.jpg"
ROOM_IMAGES_PATH = "../static/img/rooms/room_%s.jpg"

def user_visits(user_id, date_start, date_end):
    db = sqlite.connect(DATABASE_URL)
    with db:
        cur = db.cursor()
        cur.execute("""SELECT * FROM visits WHERE user_id = "%s" AND date BETWEEN "%s" AND "%s" """ % (user_id, date_start, date_end))
        rows = cur.fetchall()

    row_labels = ["user_id","room_id","date","time"]
    visits = []

    for row in rows:
        visit = dict(zip(row_labels, row))
        visit["room"] = room_info(visit["room_id"])["name"]
        visit["room_id"] = str(visit["room_id"])
        visit["date"] = ".".join(visit["date"].split("-")[::-1])
        visits.append(visit)

    return visits


def users_list():
    db = sqlite.connect(DATABASE_URL)
    with db:
        cur = db.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

    row_labels = ["id", "name", "description"]
    users = []

    for row in rows:
        user = dict(zip(row_labels, row))
        user["img"] = USER_IMAGES_PATH % user["id"]
        users.append(user)

    return users

def user_info(user_id):
    db = sqlite.connect(DATABASE_URL)
    with db:
        cur = db.cursor()
        cur.execute("""SELECT * FROM users WHERE id = "%s" """ % user_id)
        row = cur.fetchone()

    row_labels = ["id", "name", "description"]

    user = dict(zip(row_labels, row))
    user["img"] = USER_IMAGES_PATH % user["id"]
    user["description"] = json.loads(user["description"])

    return user


def rooms_list():
    db = sqlite.connect(DATABASE_URL)
    with db:
        cur = db.cursor()
        cur.execute("SELECT * FROM rooms")
        rows = cur.fetchall()

    row_labels = ["id", "name", "description"]
    rooms = []

    for row in rows:
        room = dict(zip(row_labels, row))
        room["img"] = ROOM_IMAGES_PATH % room["id"]
        rooms.append(room)

    return rooms

def room_info(room_id):
    db = sqlite.connect(DATABASE_URL)
    with db:
        cur = db.cursor()
        cur.execute("""SELECT * FROM rooms WHERE id = "%s" """ % room_id)
        row = cur.fetchone()

    row_labels = ["id", "name", "description"]

    room = dict(zip(row_labels, row))
    room["img"] = ROOM_IMAGES_PATH % room["id"]
    room["description"] = json.loads(room["description"])

    return room


def room_visits(room_id, date_start, date_end):
    db = sqlite.connect(DATABASE_URL)
    with db:
        cur = db.cursor()
        cur.execute("""SELECT * FROM visits WHERE room_id = "%s" AND date BETWEEN "%s" AND "%s" """ % (room_id, date_start, date_end))
        rows = cur.fetchall()

    row_labels = ["user_id","room_id", "date", "time"]
    visits = []

    for row in rows:
        visit = dict(zip(row_labels, row))
        visit["user"] = user_info(visit["user_id"])["name"]
        visit["date"] = ".".join(visit["date"].split("-")[::-1])
        visit["user_id"] = str(visit["user_id"])
        visits.append(visit)

    return visits


def new_visit(user_id = None, rfid_id = None, room_id = None):
    db = sqlite.connect(DATABASE_URL)
    visit_time = time.strftime("%H:%M")
    visit_date = time.strftime("%Y-%m-%d")

    with db:
        cur = db.cursor()
        if user_id is None:
            cur.execute("""SELECT id FROM users WHERE rfid_id = "%s" """ % rfid_id)
            user_id = cur.fetchone()

            if not user_id: return {}
            user_id = user_id[0]

        cur.execute("""INSERT INTO visits VALUES("%s","%s","%s","%s")""" % (user_id, room_id, visit_date, visit_time))

    return {"rfid":rfid_id, "user":user_id, "room":room_id, "date":visit_date, "time":visit_time}
