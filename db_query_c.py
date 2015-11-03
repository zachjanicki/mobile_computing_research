#!/usr/bin/python
import time

def query():
    query_dict = {  1 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 700000000000 AND Time_Stamp > 0 AND Time_Stamp < 10000000000000000',
                    2 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 800000000000 AND Sensor_ID = 400000000000',
                    3 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 400000000000 AND Sensor_ID = 700000000000 AND Value > 5000000000000000000',
                    4 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 300000000000 AND Sensor_ID = 900000000000 AND Time_Stamp > 43300',
                    5 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 100000000000 AND Sensor_ID = 300000000000 AND id > 1000000000' }
    time_list = [0]*len(query_dict)
    tests = 10
    average = 0
    for i in xrange(len(time_list)):
        for j in xrange(tests):
            start_time = time.time()
            c_data.run_sql(query_dict[i])
            end_time = time.time()
            average += end_time - start_time
        average /= tests
        time_list[i] = average