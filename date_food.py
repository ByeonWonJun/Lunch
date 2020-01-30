import sqlite3
import datetime


Adb = sqlite3.connect('Ate.db')
Acurs = Adb.cursor()

#오늘 날짜 가져오기
def get_date():
    today = datetime.date.today()
    return today

#어제 날짜 가져오기
def get_yesterday():
    yesterday = datetime.date.today() -datetime.timedelta(1)
    return yesterday

#데이터베이스에 추가
def set_date(object):
    Acurs.execute("insert into AteLunch values(?,?)",(datetime.date.today(),object))

#데이터베이스에 오늘 날짜 레코드 삭제
def delete_food():
    Acurs.execute("delete from AteLunch where day_ = '{}'".format(get_date()))
    
#전체 조회
def serch_all():
    Acurs.execute("select * from AteLunch")
    rows = Acurs.fetchall()
    for row in rows:
        print(row)

def close_db():
    Acurs.close()
    Adb.close()