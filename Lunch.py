import sqlite3
import random

def not_ate_breakfast():
    db = sqlite3.connect('LunchMenu.db')
    curs = db.cursor()    
    curs.execute("select food from FoodName where type = 'k_food';")
    rows = curs.fetchall()
    random_rows = random.choice(rows)
    db.close()
    return random_rows[0]
    
    

def ate_breakfast():
    db = sqlite3.connect('LunchMenu.db')
    curs = db.cursor() 
    curs.execute("select food from FoodName")
    rows = curs.fetchall()
    random_rows = random.choice(rows)
    db.close()
    return random_rows[0]
    
    

    
    

