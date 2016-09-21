# -*- coding: utf-8 -*- ?
from flask import Flask

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.config.from_object("config")

from app import views