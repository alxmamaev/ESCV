# -*- coding: utf-8 -*- ?
import config 
import json 
import os.path
import codecs
#база данных
db = {}

# Чтение базы данных
def load_db():
    global db
    if os.path.exists(config.data_base):
        db_file = open(config.data_base)
        db = json.loads(db_file.read().strip())
        db_file.close()
        print("База данных загружена!")
    else:
        print("База данных не обнаружена, при сохранении будет создана новая.")
# Добавление пользователя в базу данных
def add_user():
    global db
    user_id = input("Введите идентификатор пользователя: ")
    user_name = input("Введите имя пользователя: ")
    db[user_id] = user_name
    print("Пользователь успешно добавлен!")

# Вывести список пользователей
def list_user():
    print("===Список пользователей===")
    for key in list(db.keys()):
        print(db[key],":",key)

# Удаление пользователя 
def del_user():
    global db
    user_id = input("Введите идентификатор пользователя: ")
    if db.get(user_id) is None:
        print("Данного пользователя не существует!")
    else:
        print("Пользователь %s успешно удален!"%db.pop(user_id))
        
# Сохранение базы данных
def save_db():
    db_file = open(config.data_base,"w")
    db_file.write(json.dumps(db))
    db_file.close()
    print("База данных сохранена!")
    
# Просто проверка :D
def ping():
    print("понг")

def help():
    print("""
Для использования просто введите команду и следуйте указанным инструкциям.
* доб_польз - добавить пользователя
* уд_польз - удалить пользователя
* спис_польз - вывести список пользователей
* сохр - сохранить базу данных после добавления пользователя
* дек_лог - декодироватьлог файл
* вых - выход из программы
    """)

# Декодирование лог-файла в html
def decode_log():
    url = input("Введите путь до лог-файла: ")
    log_file = open(url,"r")
    log = log_file.readlines()
    log_file.close
    
    html_out = """
<!DOCTYPE html>
<html>
<head>
    <title>%s</title>
    <meta charset="utf-8">
</head>
    <body>
        <center>
            <table width = "640" border = "1">
                <tr>
                    <td><center><b>%s - Сгенерированно на основе ЭСУП</b></center></td>
                </tr>
                %s
            </table>
        </center>
    </body>
</html>
"""
    table = ""
    for row in log:
        (user_id,time) = row.split()
        user_name = db.get(user_id)
        if user_name is None: user_name = "Неизвестный пользователь (%s)"%user_id
        table += "<tr><td>%s</td><td>%s</td></tr>\n"%(user_name,time)
    
    file_name = input("Введите имя файла: ")
    doc_name = input("Введите официальное название документа: ")
    html_out = html_out%(file_name,doc_name,table)
    
    html_file = codecs.open("html_out/%s.html"%file_name,"w","utf_8")
    html_file.write(html_out)
    html_file.close()
    print("Файл успешно декодирован. Декодированный файл находится по поути корневая_директория_программы/html_out/%s.html"%file_name)

def parser():
    cmd = {
    "доб_польз":add_user,
    "уд_польз":del_user,
    "спис_польз":list_user,
    "сохр":save_db,
    "вых":exit,
    "дек_лог":decode_log,
    "пинг":ping,
    "помощь":help
    }
    while True is True:
        print()
        comand = input("Введите команду: ")
        if cmd.get(comand) is None:
            print("Не корректная команда, что-бы узнать список команд введите 'помощь'")
        else:
            cmd[comand]()
def main(): 
    print("Добро пожаловать в программу для декодирования лог файлов ЭСУПv2")
    load_db()
    parser()

if __name__ == "__main__": main()