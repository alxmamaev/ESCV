# -*- coding: utf-8 -*-
import random
import pandas as pd
from app import base

def to_csv(visits):
    file_name = "export\\%s.csv" % hex(random.randint(0, 1000000))
    visits = pd.DataFrame(visits)
    visits.pop("user_id")
    visits.pop("room_id")
    visits.to_csv("app\\"+file_name, index=False)
    return file_name