import sqlite3


conn = sqlite3.connect('webtext.db')
c = conn.cursor()
textentry = "SELECT * FROM webtext"



def tableCreate():
    c.execute("CREATE TABLE webtext (ID INTEGER PRIMARY KEY, bodytext BLOB)")

def dropTable():
    c.execute ("DROP TABLE IF EXISTS webtext")

def dataEntry(bodyText):
    c.execute("INSERT INTO webtext (bodytext) VALUES ('{}')".format(bodyText))
    conn.commit()

def readData():
    for row in c.execute(textentry):
        return row

def fetchRecord():
    
    list_loadr = c.execute('''SELECT * FROM webtext''')
    list_load = list_loadr.fetchall()
    return list_load
    
