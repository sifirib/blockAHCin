import datetime
import sqlite3
import os
import shutil
from tkinter import *








# path = "/home/hrx/Desktop/projects/python/ahcoin/users.db"
# connection = sqlite3.connect(path)

# cursor = connection.execute("SELECT id, wallet, cash from USERS")

##########################################  WALLETS
# def wallets():
#     list = os.listdir(path)
#     number_of_files = len(list)  
#     wallets = []
#     for i in range(1,number_of_files + 1):
#         conn = sqlite3.connect(f"{path}/user{i}.db")
#         c = conn.cursor()
#         wallet = c.execute(f'''SELECT wallet FROM users''')
#         wallets.append(wallet)
#     return wallets

###########################################################

coinname = 'AHCoin'

path = "/home/hrx/Desktop/projects/python/ahcoin/databases" ### Set the path variable to where the python file is.

class person:
    
    
    def __init__(self, name = 'denemehesap', cash = 1000, date_of_record = 301220, wallet = '', amount_of_money = 0):
        self.name = name 
        self.cash = cash
        self.dor = date_of_record
        self.aom = amount_of_money
        self.wallet = [((self.name[i] + (str(self.dor) + '1327559486')[i])) for i in range(len(self.name)) ]



def verification_old():
    list = os.listdir(path)
    number_of_files = len(list)
    wallets = []
    cashes = []
    aoms = []
    
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        c = conn.cursor()
        wallet = c.execute(f'''SELECT wallet FROM users WHERE "id = {i}"''')
        wallets.append(wallet)
        cash = c.execute(f'''SELECT cash FROM users WHERE "id = {i}"''')
        cashes.append(cash)
        aom = c.execute(f'''SELECT amount_of_money FROM users WHERE "id = {i}"''')
        aoms.append(aom)
       
    if wallets.count(wallet) > number_of_files:
        if cashes.count(cash) > number_of_files:
            if aoms.count(aom) > number_of_files:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    

                

def db_copy(name_of_file):
    list = os.listdir(path)
    number_of_files = len(list)
    original = rf'{path}/{name_of_file}'     
    target = rf'{path}/user{number_of_files + 1}.db'
    shutil.copyfile(original, target)


# def db_create():
    
    
#     list = os.listdir(path)
#     number_of_files = len(list)
#     i = number_of_files + 1
#     conn = sqlite3.connect(f"{path}/user{i}.db")
#     c = conn.cursor()
#     c.execute('''CREATE TABLE users
#              ([id] integer, [wallet] text, [cash] integer, [amount_of_money] integer)''')
#     conn.commit()

   
    
    
# def id_setter():
#   cursor = conn.execute("SELECT id from USERS")
#   id = 1
#   for row in cursor:
#       id += 1
#   return id


def signup():
    name = str(walletkayit.get)
    dor = datetime.datetime.now()
    dor = str(dor.day) + str(dor.month) + str(dor.year)
    naccount = person()
    naccount.name = name
    naccount.dor = dor
    naccount.wallet = [(naccount.name[i] + (naccount.dor + '1327559486')[i]) for i in range(len(naccount.name))] 
    naccount.wallet = "".join(naccount.wallet)

    # db_create()
    
    db_copy('user1.db')
    
    
    list = os.listdir(path)
    number_of_files = len(list)
    
    conn = sqlite3.connect(f"{path}/user1.db")
    c = conn.cursor()
    aom_for_newuser = f"""SELECT amount_of_money FROM users WHERE id = 1 """
    c.execute(aom_for_newuser)
    aom_for_newuser = c.fetchone()[0]
    conn.commit()
        
    for i in range(number_of_files, 0, -1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        sql = f"""INSERT INTO users(id, wallet, cash, amount_of_money)
        VALUES ({number_of_files}, '{naccount.wallet}', {naccount.cash}, {naccount.aom});"""
        cursor = conn.cursor()
        cursor.execute(sql)
        sqlmiktar = f"""UPDATE users
        SET amount_of_money = {aom_for_newuser} WHERE wallet = '{naccount.wallet}'
        """
        cursor.execute(sqlmiktar)
        conn.commit()
        


    print(f"Wallet adresiniz: {naccount.wallet}\n","Giris yapmak icin uygulamayi tekrar baslatiniz.")
    
    # connection.execute(f"UPDATE USERS SET wallet = {naccount.wallet} where 'id = 3'")
    # connection.execuwalletste("UPDATE USERS SET cash = 100 where ID = 3")
    
    # return cursor.lastrowid  


    


def amount_update(amount):
       
    list = os.listdir(path)
    number_of_files = len(list)
    
        
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        sql = f"""UPDATE users
        SET amount_of_money = {amount};
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

def gcash_update(gonderen, miktar):
    list = os.listdir(path)
    number_of_files = len(list)

    
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        c = conn.cursor()
        sql1 = f"""SELECT cash FROM users WHERE wallet = '{gonderen}'"""
        c.execute(sql1)
        oldcash = c.fetchone()[0]
        newcash = oldcash - miktar
        sql = f'''UPDATE users
        SET cash = {newcash}       
        WHERE wallet = "{gonderen}"'''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        
def acash_update(alan, miktar):
    list = os.listdir(path)
    number_of_files = len(list)
            
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        c = conn.cursor()
        sql1 = f"""SELECT cash FROM users WHERE wallet = '{alan}'"""
        c.execute(sql1)
        oldcash = c.fetchone()[0]
        newcash = oldcash + miktar
        sql = f'''UPDATE users
        SET cash = {newcash}       
        WHERE wallet = "{alan}"'''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
     



def signin():
    
 
    
    userwallet = walletgiris.get()
   
    # list = os.listdir(path)
    # number_of_files = len(list)
    walletss = []

    conn = sqlite3.connect(f"{path}/user1.db")
    c = conn.cursor()
    c.execute(f'''SELECT wallet FROM users''')
    # df.wallet = df.wallet.astype(str)
    results = c.fetchall()
    count = len(results)
    for i in range(0, count):
        result = str(results[i][0])
        walletss.append(result)
  
        
    for row in walletss:
        
        if userwallet == row:
            print("Basariyla giris yaptiniz.")
            currentuser = userwallet
            break
        else:
            print("Kullanici bulunamadi.")
            
    
    


        
    def sendcoin():
        gonderen = currentuser
        alan = input("Alicinin Wallet adresi: ")
        miktar = int(input("Miktar: "))
        amount_update(miktar)
        
        def shasher(hashh):
            thash = ''
            i = 0
            hashh += hashh
            hashh += hashh
            while len(thash) < 23:
                thash += hashh[i]
                
                i += 2
            return thash
        
        
        def hasher(gwallet, awallet, miktar):
            hashh = ''
            i = 0
            k = 0
       
            miktar *= 78
            smiktar = str(miktar)
            limit = min(len(gwallet),len(awallet))
            
            while len(hashh) < 21:
                l = smiktar[k]
                
                
                hashh += gwallet[i] + awallet[i] + l
                i += 1
                k += 1
                
                if i == limit:
                    i = 0
                if k == len(str(smiktar)):
                    k = 0
            return shasher(hashh)
        
        
        def verification():
            list = os.listdir(path)
            number_of_files = len(list)
            
            thehash = hasher(gonderen, alan, miktar)
            aim_of_verification = 0
            for i in range(1,number_of_files + 1):
                conn = sqlite3.connect(f"{path}/user{i}.db")
                c = conn.cursor()
                # cash = c.execute(f'''SELECT cash FROM users WHERE wallet = "{gonderen}"''')
                c.execute(f'''SELECT amount_of_money FROM users WHERE wallet = "{gonderen}"''')
                aom = c.fetchone()[0]
                aom = float(aom)
                aom = int(aom)
                hashhh = hasher(gonderen, alan, aom)
                if hashhh == thehash:
                    aim_of_verification += 1
            
            if aim_of_verification > (number_of_files/2):
                return True
            else:
                return False
        
        # billhash = hasher(gonderen, alan, miktar)
            
        date_of_theprocess = datetime.datetime.now()
        date_of_theprocess = str(date_of_theprocess.day) + "/" + str(date_of_theprocess.month) + "/" + str(date_of_theprocess.year) + " " + str(date_of_theprocess.hour)  + ":" + str(date_of_theprocess.minute)  
               
        miktarrr = miktar
        if verification():
            acash_update(alan, miktarrr), gcash_update(gonderen, miktarrr)
            print("Islem basariyla dogrulandi")
            print(f"""
                     Makbuz: 
                     
                     Gonderen: {gonderen}
                     Alan : {alan}
                     Miktar: {miktar} {coinname} 
                     Tarih: {date_of_theprocess}
                     """)
        else:
            print("Islem dogrulanamadi!!!")
            
            
          
            
    secim = input(f"{coinname} gondermek icin gonder yaziniz: ")
    
    if secim == 'gonder':
        

            sendcoin()

        
value = 2
          
def buttonvalue(x):
    value = x
    return value


print(" "*20 + coinname)
first_screen = Tk()
upp = Button(first_screen, text = 'Kayit', command = buttonvalue(1))
inn = Button(first_screen, text = 'Giris', command = buttonvalue(0))
upp.pack()
inn.pack()

first_screen.mainloop()

print(value)

if value == 0:
    
    userwallet = Label(first_screen, text = "Wallet Adresi: ")
    userwallet.grid(row = 0, column = 0)
    walletgiris = Entry(first_screen, width="20")
    walletgiris.grid(row=0, column=1)
    
    benihatirla = Checkbutton(first_screen,text="beni hatırla")
    benihatirla.grid(row = 2, columnspan = 2)
    walletgiriss = Button(first_screen,text="giriş", command = signin)
    walletgiriss.grid(row = 3, column = 1)
    
    first_screen.mainloop()
    
elif value == 1:
    nameyazi = Label(first_screen,text = "Ad: ")
    nameyazi.grid(row = 0, column = 0)
    namekayit = Entry(first_screen, width="20")
    namekayit.grid(row = 0, column = 1)
    
    walletkayit = Button(first_screen, text = "kayit ol", command = signup)
    walletkayit.grid(row = 3, column = 1)
    first_screen.mainloop()
    

    
    
else:
    print('yanlis komut girdiniz!')




# cursor = connection.execute("SELECT id, wallet, cash from USERS")
# for row in cursor:
#     print(row[0])
#     print(row[1])
#     print(row[2])


# if gonderen.name == 'denemehesap':
#     print('Deneme hesabi ile yapacaginiz islemler gerceklestirilmeyecektir.')



# user2 = input("Alici kisinin Wallet adresi: ")
# miktar = int(input("Miktar: "))

# user2 = person(user2)



##### HASHERS FOR VERIFICATION PROCESSES(if the hash equals for all users, the process will verificate)



################################

        





