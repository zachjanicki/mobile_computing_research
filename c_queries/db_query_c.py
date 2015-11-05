#!/usr/bin/python
import time

'''list of c functions: 
    run_sql - takes in sql command as string and executes it
    grow_db - increases db size by 1m rows
    revert_db - puts db back to 0 rows
    shrink_db - decreases db size by 1m rows
    '''

def query():
    query_dict = {  1 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 700000000000 AND Time_Stamp > 0 AND Time_Stamp < 10000000000000000',
                    2 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 800000000000 AND Sensor_ID = 400000000000',
                    3 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 400000000000 AND Sensor_ID = 700000000000 AND Value > 5000000000000000000',
                    4 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 300000000000 AND Sensor_ID = 900000000000 AND Time_Stamp > 43300',
                    5 : 'SELECT * FROM Data_Collection WHERE Dev_ID = 100000000000 AND Sensor_ID = 300000000000 AND id > 1000000000' }
    time_list = [[]]*len(query_dict)
    growths = 10
    tests = 10
    average = 0
    for i in xrange(len(time_list)):
        for j in xrange(tests):
            for k in range(growths):
                c_data.grow_db()
                start_time = time.time()
                c_data.run_sql(query_dict[i])
                end_time = time.time()
                average += end_time - start_time
            average /= tests
            time_list[i][growths] = average
            average = 0