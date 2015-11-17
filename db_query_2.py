#!/usr/bin/python
import time, sqlite3, random, numpy, matplotlib.pyplot as plt

db_path = '/Users/zachjanicki/Developer/Poellabauer/mobile_computing_research/data.sqlite'
growths = 20
tests = 10000
query_dict = {  1 : 'SELECT * FROM Data_Collection WHERE Device_ID = 700000000000 AND Time_Stamp > 0 AND Time_Stamp < 43300 ORDER BY Device_ID DESC',
                2 : 'SELECT * FROM Data_Collection WHERE Device_ID = 800000000000 AND Sensor_ID = 400000000000',
                3 : 'SELECT * FROM Data_Collection WHERE Device_ID = 400000000000 AND Sensor_ID = 700000000000 AND Value > 5000000000000000000',
                4 : 'SELECT * FROM Data_Collection WHERE Device_ID = 300000000000 AND Sensor_ID = 900000000000 AND Time_Stamp > 43300',
                5 : 'SELECT * FROM Data_Collection WHERE Device_ID = 100000000000 AND Sensor_ID = 300000000000 AND id > 1000000000' }
'''list of functions: 
    run_sql - takes in sql command as string and executes it
    grow_db - increases db size by 1m rows
    destroy_db - puts db back to 0 rows
    shrink_db - decreases db size by 1m rows
    graph - takes in average_list and st_dev_list and plots each 
    '''

def query():
    ''' Runs each query 10 times and then increases the size of the database.
        Calculates average query time, and std dev from average''' 
    time_list = [[]]*len(query_dict)
    average = 0
    times = []
    all_times = []
    for i in xrange(len(time_list)):
        for j in xrange(growths):
            grow_db()
            for k in range(tests):
                start_time = time.time()
                run_sql(query_dict[i+1])
                end_time = time.time()
                times.append(end_time - start_time)
                average += end_time - start_time
                
            average /= tests
            time_list[i].append(average)
            all_times.append(times)
            times =  []
            average = 0
            destroy_db()
            
    # get averages, and standard deviation        
    std_dev_list = []
    average_list = []
    for i in range(len(query_dict) * growths):
        std_dev_list.append(numpy.std(all_times[i]))
        average_list.append(numpy.mean(all_times[i]))
    print std_dev_list
    print average_list
    
    
    return average_list, std_dev_list
            
def run_sql(sql):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(sql)
    c.fetchall()
    
def grow_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    with conn:
        for i in range(100):
            row_data = []
            row_id = i
            dev_id = random.randint(0, 10)
            sens_id = random.randint(0, 10) * (10**11)
            time_stamp = random.randint(0, 86400)
            val = str(random.randint(0, 9223372036854775807))
            dev_id *= 100000000000
            row_data.append(row_id)
            row_data.append(dev_id)
            row_data.append(sens_id)
            row_data.append(time_stamp)
            row_data.append(val)
            c.executemany("INSERT INTO Data_Collection VALUES(?,?,?,?,?)", (row_data,))
    print "successful growth"
def shrink_db():
    pass
    
def create():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""CREATE TABLE Data_Collection(id int, Device_ID int, Sensor_ID int, Time_Stamp int, Value char)""")
    conn.commit()
    conn.close()
    
def destroy_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""DELETE FROM Data_Collection""")
    conn.commit()
    conn.close()
    
def graph(average_list, std_dev_list):
        
    for i in xrange(len(query_dict)+1):
        if i == 5:
            continue
        plt.figure(i)
        x_axis_points = [x for x in range(1, growths+1)]
        y_axis_points = average_list[i*growths:i*growths+growths]
        print len(x_axis_points), len(y_axis_points)
        plt.plot(x_axis_points, y_axis_points, 'ro')
        # get list of points with std_dev added
        std_dev_points = [average_list[j] + std_dev_list[j] for j in range(growths*i, growths*i + growths)]
        plt.plot(x_axis_points, std_dev_points, 'bo')
        std_dev_points = []
        # get list of points with std_dev subtracted
        std_dev_points = [average_list[j] - std_dev_list[j] for j in range(growths*i, growths*i + growths)]
        plt.plot(x_axis_points, std_dev_points, 'bo')
        y_axis_points = []
        x_axis_points = []
        std_dev_points = []
        
def main():
    destroy_db()
    x, y = query()
    graph(x, y)