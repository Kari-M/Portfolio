import sqlite3
import time
import datetime


conn = sqlite3.connect('filetrans.db')
c = conn.cursor()
lastRecord = "SELECT MAX(datestamp) FROM fileTransTime"




def tableCreate():
    c.execute("CREATE TABLE fileTransTime (ID INTEGER PRIMARY KEY, unix REAL, datestamp TEXT)")

def dropTable():
    c.execute("DROP TABLE IF EXISTS fileTransTime")
    
def dataEntry():
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%b-%d %H:%M:%S'))
    c.execute("INSERT INTO fileTransTime (unix, datestamp) VALUES (?,?)",
              (time.time(), date,))
    conn.commit()

def readData():
    for row in c.execute(lastRecord):
        return row
    
