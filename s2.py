import sqlite3
try:
    sqlite_Connection = sqlite3.connect('mydb1.db')
    conn = sqlite_Connection.cursor()
    print('\nDatabase created and connected to sqlite')
    sql_query = "select sqlite_version();"
    conn.execute(sql_query)
    record = conn.fetchall()
    print("the record it fetched and sqlite version is ",record)
    conn.close()



except sqlite3.Error as error :
    print("\nError while connecting to sqlite")


finally:
    if(sqlite_Connection):
        sqlite_Connection.close()
        print("\n Sqlite connection closed")