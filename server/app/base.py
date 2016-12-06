# -*- coding: utf-8 -*- ?
import sqlite3 as sqlite
import config
from app import app
import time
import logging

def user_visits(user_id, date_start, date_end):
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    
    cur.execute("""SELECT * FROM visits WHERE user_id=%s AND date>="%s" AND date<="%s" """ % (user_id, date_start, date_end))
    rows = cur.fetchall()
    row_labels = ["user_id","room_id", "date", "time"]
    visits = []
    
    for row in rows:
        visit = dict(zip(row_labels, row))
        visit["room"] = room_info(visit["room_id"])["name"]
        visit["room_id"] = str(visit["room_id"])
        visit["date"] = ".".join(visit["date"].split("-")[::-1])

        visits.append(visit)
        
    return visits
    

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
    cur.execute("SELECT * FROM users WHERE id = %s" % user_id)
    
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
    cur.execute("SELECT * FROM rooms WHERE id = %s" % room_id)
    
    row_labels = ["id", "name", "description"]
    row = cur.fetchone()

    room = dict(zip(row_labels, row)) 
    room["img"] = config.room_img_url % room["id"]

    return room


def room_visits(room_id, date_start, date_end):
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    cur.execute("""SELECT * FROM visits WHERE room_id=%s AND date>="%s" AND date<="%s" """ % (room_id, date_start, date_end))    
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


def new_visit(user_id=None, rfid_id=None, room_id=None):
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    
    visit_time = time.strftime("%H:%M") 
    visit_date = time.strftime("%Y-%m-%d")
    
    if user_id is None:
        cur.execute("SELECT id FROM users WHERE rfid_id = %s" % rfid_id)
        user_id = cur.fetchone()
        if user_id is not None: user_id = user_id[0]
        else: return 1     
    
    with db:
        cur.execute("INSERT INTO visits VALUES(?,?,?,?)", (user_id, room_id, 
                                                           visit_date, visit_time))

    return "|rfid:%s|user:%s|room:%s|date:%s|time:%s|" % (rfid_id, user_id, room_id, 
                                                               visit_date, visit_time)