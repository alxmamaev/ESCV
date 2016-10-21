# -*- coding: utf-8 -*- ?
import sqlite3 as sqlite

def users_list():
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM users")
    
    row_labels = ["id", "name", "description"]
    rows = cur.fetchall()
    
    users = []
    for row in rows:
        user = dict(zip(row_labels, row)) 
        user["img"] = "../static/img/user_%s.jpg" % user["id"]
        users.append(user)
    
    return users

def user_info(user_id):
    db = sqlite.connect("escv.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    
    row_labels = ["id", "name", "description"]
    row = cur.fetchone()

    user = dict(zip(row_labels, row)) 
    user["img"] = "../static/img/user_%s.jpg" % user["id"]

    return user    
