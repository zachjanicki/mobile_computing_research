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
    set 4: rows - 10m to 50m
