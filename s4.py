import sys
import time
import csv
import sqlite3



def waittime3():
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)

try:
    #Importing 
    print("opening csv file to read")
    waittime3()
    with open('student_info.csv','r') as fin:
        dr = csv.DictReader(fin)
        student_info = [(i['id'],i['name'],i['age'],i['phone']) for i in dr]
        print("Printing csv that is read")
        waittime3()
        print(student_info)

    #connect to sqlite

    sqlite_Connection = sqlite3.connect('mydb1.db')
    cursor = sqlite_Connection.cursor()
    print('\nSuccessfully connected to db')

    #create student table

    cursor.execute('create table stu_info(id int, name varchar(20),age int, phone int)')
    print('stu_info table is created successfully')
    waittime3()

    #insert data into table

    cursor.executemany(
        "insert into stu_info(id,name,age,phone) values(?,?,?,?)", student_info)
    print("Successfully inserted data into student table")

    #show student table

    cursor.execute("select * from stu_info")
    print("Retrieving the data")

    #view the results of the retrieved data

    result = cursor.fetchall()
    print("Preparing to display the data")


    print(result)

    #commit the work and close the connection

    sqlite_Connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error occured : ",error)

finally:
    if sqlite_Connection:
        sqlite_Connection.close()
        print("\n Sqlite connection closed")
    


    
