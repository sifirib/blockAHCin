import os
import sqlite3
path = "/home/hrx/Desktop/projects/python/ahcoin/databases" 
list = os.listdir(path)
number_of_files = len(list)
    
for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        sql = f"""UPDATE users
        SET cash = 1000, amount_of_money = 0
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()