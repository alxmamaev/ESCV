import sqlite3
import os

DATABASE_URL = os.environ.get("DATABASE_URL", default = "escv.db")

def setup_database():
    os.remove(DATABASE_URL)
    db = sqlite3.connect(DATABASE_URL)
    with db:
        cur = db.cursor()
        cur.execute("CREATE TABLE `rooms` (`id`	INTEGER,`name`	TEXT, `description`	TEXT, PRIMARY KEY(`id`));")
        cur.execute("CREATE TABLE `users` (`id`	INTEGER,`name`	TEXT,`description`	TEXT,`rfid_id`	TEXT,PRIMARY KEY(`id`));")
        cur.execute("CREATE TABLE `visits` (`user_id`	INTEGER,`room_id`	INTEGER,`date`	TEXT,`time`	TEXT);")

def main():
    setup_database()

if __name__=="__main__": main()
