import sys
import time
import csv
import sqlite3


def waittime5():
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
def waittime3():
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)


def test():
    print("opening csv file to read")
    waittime3()
    with open('student_info.csv','r') as fin:
        dr = csv.DictReader(fin)
        student_info = [(i['id'],i['name'],i['age'],i['phone']) for i in dr]
        print("Printing csv that is read")
        waittime3()
        print(student_info)

test()

