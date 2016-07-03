# -*- coding: utf-8 -*- ?
import os
import socket 

# Здесь коментарии излишни

def main():
    print("Добро пожаловать в программу для работы с ЭСУПv3")
    if len(socket.gethostbyname_ex(socket.gethostname())[2]) > 1:
        print("Сервер запущен на адресе: %s"%socket.gethostbyname_ex(socket.gethostname())[2][1])
        from http.server import HTTPServer, CGIHTTPRequestHandler
        server_address = ("", 80)
        httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
        httpd.serve_forever()
    else: input("Ошибка! Не удалось подключится к сети.")
if __name__ == "__main__": main()