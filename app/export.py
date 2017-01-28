# -*- coding: utf-8 -*-
import os
import random
import pandas as pd
from app import base

def to_csv(visits):
    file_name = "export/%s.csv" % hex(random.randint(0, 1000000))
    visits = pd.DataFrame(visits)
    if visits.get("user_id") is not None: visits.pop("user_id")
    if visits.get("room_id") is not None: visits.pop("room_id")
    visits.to_csv(file_name, index=False)
    return os.path.abspath(file_name)
