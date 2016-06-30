#!/usr/bin/env python3
# -*- coding: utf-8 -*- ?
import cgi
import time
import config
import os.path
import time
import codecs

def add_entry(user_name):
    print("Content-type: text/html\n")
    print("Hello: "+user_name) 
    
    user_time = ":".join(map(str,time.localtime()[3:5])) 
    file_name = config.out_dir + "_".join(map(str,time.localtime()[0:3])) + ".html"
    entry = "<tr><td>%s</td><td>%s</td></tr>\n" % (user_name,user_time) + "%s"
    
    if os.path.exists(file_name):
        html_table = codecs.open(file_name,"r","utf-8").read()
        html_file = codecs.open(file_name,"w","utf-8")    
        html_file.write(html_table % entry)
    else:
        html_file = codecs.open(file_name,"w","utf-8")
        discription = "Отчет за "+".".join(map(str,time.localtime()[0:3]))
        html_table = """
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
        html_file.write(html_table % (discription, discription, entry))
        
    html_file.close()        
        
def main():
    
    form = cgi.FieldStorage()
    rfid_id = form.getfirst("rfid_id", None)
    
    if rfid_id is None:
        add_entry("Test_User")
    else:
        data_base = open(config.data_base,"r").readlines()
        for user in data_base:
            (user_id,user_name) = user.strip().split()      
            if user_id == rfid_id:                 
                add_entry(user_name)
                break
        else: add_entry("Неизвестный полльзователь (%s)" % user_id)
main()
