import Lunch
import sqlite3
import random
import date_food


while True:
    print("""
    ---------------------------
          1  점심 등록
          2  오늘 점심 삭제
          3  어제 점심 조회
          4  총 점심 조회
          5  종료
    ---------------------------""")

    num = input()

    if num == '1':
        print("""
    ---------------------------
     아침 먹었나요?(Y/N) 종료(A)
    ---------------------------""")
        breakfast=input()

        if breakfast in ['y','Y']:
            lunch = Lunch.ate_breakfast()
            print(lunch)
            print("점심 메뉴로 정하시겠습니까?(Y/N)")
            try:
                menu = input()
                if menu in ['y','Y']:
                    date_food.set_date(lunch)
                    print(date_food.get_date(),"점심메뉴로 등록 되었습니다.")
                    date_food.close_db()
                    break
            except:
                print("이미 오늘의 점심메뉴가 등록 되어있습니다.")
        

        elif breakfast in ['n','N']:
            lunch = Lunch.not_ate_breakfast()
            print(lunch)
            print("점심 메뉴로 정하시겠습니까?")
            try:
                menu = input()
                if menu in ['y','Y']:
                    date_food.set_date(lunch)
                    print(date_food.get_date(),"점심메뉴로 등록 되었습니다.")
                    date_food.close_db()
                    break
            except:
                print("이미 오늘의 점심메뉴가 등록 되어있습니다.")

        elif breakfast in ['a','A']:
            break
        else:
            print("잘못 입력하셨습니다")
    
    if num == '2':
        date_food.delete_food()
        print("오늘의 메뉴가 삭제 되었습니다.")
    
    if num == '3':
        date_food.serch_yesterday()

    if num == '4':
        date_food.serch_all()
    
    if num == '5':
        date_food.close_db()
        break



    


    