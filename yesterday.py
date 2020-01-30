import sqlite3
import datetime


Adb = sqlite3.connect('Ate.db')
Acurs = Adb.cursor()

def get_date():
    today = datetime.date.today()
    return today

def get_yesterday():
    yesterday = datetime.date.today() -datetime.timedelta(1)
    return yesterday

def set_date(object):
    Acurs.execute("insert into AteLunch values(?,?)",(datetime.date.today(),object))
    Adb.commit()
    Adb.close()


    
    