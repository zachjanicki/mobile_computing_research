''' Fields: id (int 11), Device_ID (bigint 20), Sensor_ID (int),
Time_Stamp (bigint 20), Value (varchar 1000)

Test Queries:
    SELECT * FROM table_name WHERE Sensor_ID = sens_id
    SELECT * FROM table_name WHERE Value = val
    SELECT * FROM table_name WHERE Sensor_ID = sens_id AND Value = val
    SELECT * FROM table_name WHERE Time_Stamp > time_1 AND Time_Stamp < time_2
    SELECT * FROM table_name WHERE Sensor_ID = sens_id AND Value < val
    SELECT * FROM table_name WHERE Time_Stamp = time
    
Alternate Schema ideas:
    - all data as varchar's
    - var char's instead of big ints
    
Table sizes:
    set 1: rows - 10k to 50k
    set 2: rows - 100k to 500k
    set 3: rows - 1m to 5m
'''

import sqlite3
import time
import random
import matplotlib.pyplot as plt

db_path = '/Users/zachjanicki/Developer/Poellabauer/mobile_computing_research/data'
def create_tables(): 
    for i in range(1, 4):
        conn = sqlite3.connect(db_path+ str(i) + '.sqlite')
        c = conn.cursor()
        for i in range(1, 5):
            c.execute("CREATE TABLE Data_Collection"+str(i)+ 
                        "(id, Device_ID, Sensor_ID, Time_Stamp, Value)")
        conn.commit()
        conn.close()
    
def add_data_original_schema(): 
    '''add random data with certain range of values'''
    start_time = time.time()
    for i in range(1,4):
        for j in range(1, 5):
            path_append = str(i) + ".sqlite"
            conn = sqlite3.connect(db_path+path_append)
            c = conn.cursor()
            with conn:
                for k in range(j*(10**(i+3))):
                    row_data = []
                    row_id = k
                    dev_id = random.randint(0, 9223372036854775807)
                    sens_id = random.randint(0, 10)
                    time_stamp = random.randint(0, 86400)
                    val = str(random.randint(0, 9223372036854775807))
                    row_data.append(row_id)
                    row_data.append(dev_id)
                    row_data.append(sens_id)
                    row_data.append(time_stamp)
                    row_data.append(val)
                    if j == 1:
                        c.executemany("INSERT INTO Data_Collection1 VALUES(?,?,?,?,?)", (row_data,))
                    elif j == 2:
                        c.executemany("INSERT INTO Data_Collection2 VALUES(?,?,?,?,?)", (row_data,))
                    elif j == 3:
                        c.executemany("INSERT INTO Data_Collection3 VALUES(?,?,?,?,?)", (row_data,))
                    else:
                        c.executemany("INSERT INTO Data_Collection4 VALUES(?,?,?,?,?)", (row_data,))
            print time.time() - start_time
            
def query():
    '''this method will query the databases and give results that estimate time complexity
    QUERIES:
    
    SELECT * FROM table_name WHERE Sensor_ID = sens_id
    SELECT * FROM table_name WHERE Value = val
    SELECT * FROM table_name WHERE Sensor_ID = sens_id AND Value = val
    SELECT * FROM table_name WHERE Time_Stamp > time_1 AND Time_Stamp < time_2
    SELECT * FROM table_name WHERE Sensor_ID = sens_id AND Value < val
    SELECT * FROM table_name WHERE Time_Stamp = time
    
    '''
    query_time_log = [[]]
    for j in xrange(1, 4):
        conn = sqlite3.connect(db_path + str(j) +'.sqlite')
        c = conn.cursor()
    
        for i in xrange(1, 5):
            query_dict = {  1 : 'SELECT * FROM Data_Collection' + str(i) + ' WHERE Time_Stamp > 0 AND Time_Stamp < 10000000000000000',
                            2 : 'SELECT * FROM Data_Collection' + str(i) + ' WHERE Sensor_ID = 40000000000',
                            3 : 'SELECT * FROM Data_Collection' + str(i) + ' WHERE Sensor_ID = 7 AND Value > 5000000000000000000',
                            4 : 'SELECT * FROM Data_Collection' + str(i) + ' WHERE Sensor_ID = 9 AND Time_Stamp > 5000000000000000000',
                            5 : 'SELECT * FROM Data_Collection' + str(i) + ' WHERE Sensor_ID = 3 AND id > 1000000000' }
        
        
            for k in range(1, 6):
                start_time = time.time()
                c.execute(query_dict[k])
                queries = c.fetchall()
                end_time = time.time() - start_time
                query_time_log[j - 1].append(end_time)
        if j != 3:
            query_time_log.append([])
        print len(query_time_log[j-1])
    return query_time_log

def results(query_time_log):
    # reconstruct data to correlate with row size
    data_dict = {}
    query_data = []
    offset = 0
    for k in xrange(5):
        for i in xrange(3):
            for j in xrange(4):
                query_data.append(query_time_log[i][j*5 + offset])
        dict_key = 'q' + str(offset+1)
        print dict_key
        data_dict[dict_key] = query_data
        offset += 1
        print data_dict[dict_key] 
        query_data = []   
    
    for i in xrange(5):
        dict_key = 'q' + str(i + 1)
        plt.plot([1,2,3,4,10, 20, 30, 40, 100, 200, 300, 400], data_dict[dict_key], 'ro')
        #plt.axis([0, 6, 0, 20])
        plt.show()
        plt.figure(i)