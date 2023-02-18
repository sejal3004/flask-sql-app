import sys
import time
import csv
import sqlite3



def waittime3():
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)


cursor.execute("select * from stu_info")
    print("Retrieving the data")
