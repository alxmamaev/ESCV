# -*- coding: utf-8 -*- ?
import sqlite3 as sqlite
import config

def users_list():
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM users")
    
    row_labels = ["id", "name", "description"]
    rows = cur.fetchall()
    
    users = []
    for row in rows:
        user = dict(zip(row_labels, row)) 
        user["img"] = config.users_img_url % user["id"]
        users.append(user)
    
    return users

def user_info(user_id):
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    
    row_labels = ["id", "name", "description"]
    row = cur.fetchone()

    user = dict(zip(row_labels, row)) 
    user["img"] = config.users_img_url % user["id"]

    return user    


def rooms_list():
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM rooms")
    
    row_labels = ["id", "name", "description"]
    rows = cur.fetchall()
    
    rooms = []
    for row in rows:
        room = dict(zip(row_labels, row)) 
        room["img"] = config.room_img_url % room["id"]
        rooms.append(room)
    
    return rooms

def room_info(room_id):
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM rooms WHERE id = ?", (room_id,))
    
    row_labels = ["id", "name", "description"]
    row = cur.fetchone()

    room = dict(zip(row_labels, row)) 
    room["img"] = config.room_img_url % room["id"]

    return room
