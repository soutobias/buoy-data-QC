# -*- coding: utf-8 -*-
"""
created on Tue may 03 10:08:32 2016

@author: Tobias
"""
from quality_control import *
import sql_queries
import time_codes

import sys
import os
from os.path import expanduser
home = expanduser("~")
sys.path.insert(0,home)
import user_config1 as user_config
os.chdir( user_config.path )

buoys = sql_queries.working_buoys(user_config)

for buoy in buoys:
    print(buoy["nome"])

    raw_data = sql_queries.select_raw_data_bd(buoy["argos_id"], user_config)

    adjusted_data = adjust_data(raw_data)

    adjusted_data = adjust_different_message_data(adjusted_data)

    (flag_data, qc_data) = qualitycontrol(adjusted_data, buoy)

    qc_data = rotate_data(qc_data)

    delete_qc_old_data(initial_time, buoy):

    insert_qc_data_bd(qc_data, buoy, user_config)
