import datetime
import sqlite3
import os

# path = "/home/hrx/Desktop/projects/python/ahcoin/users.db"
# connection = sqlite3.connect(path)

# cursor = connection.execute("SELECT id, wallet, cash from USERS")

##########################################  WALLETS
# list = os.listdir(path)
# number_of_files = len(list)  
# wallets = []
# for i in range(1,number_of_files + 1):
#     conn = sqlite3.connect(f"{path}/user{i}.db")
#     c = conn.cursor()
#     wallet = c.execute(f'''SELECT wallet FROM users''')
#     wallets.append(wallet)
###########################################################

coinname = 'AHCoin'

path = "/home/hrx/Desktop/projects/python/ahcoin/databases"

class person:
    
    
    def __init__(self, name = 'denemehesap', cash = 1000, date_of_record = 301220, wallet = '', amount_of_money = 0):
        self.name = name 
        self.cash = cash
        self.dor = date_of_record
        self.aom = amount_of_money
        self.wallet = [((self.name[i] + (str(self.dor) + '1327559486')[i])) for i in range(len(self.name)) ]



def verification():
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
                

         
    

def db_create():
    
    
    list = os.listdir(path)
    number_of_files = len(list)
    i = number_of_files + 1
    conn = sqlite3.connect(f"{path}/user{i}.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE users
             ([id] integer, [wallet] text, [cash] integer, [amount_of_money] integer)''')
    conn.commit()

   
    
    
# def id_setter():
#   cursor = conn.execute("SELECT id from USERS")
#   id = 1
#   for row in cursor:
#       id += 1
#   return id


def signup():
    name = str(input("Ad: "))
    dor = datetime.datetime.now()
    dor = str(dor.day) + str(dor.month) + str(dor.year)
    naccount = person()
    naccount.name = name
    naccount.dor = dor
    naccount.wallet = [(naccount.name[i] + (naccount.dor + '1327559486')[i]) for i in range(len(naccount.name))] 
    naccount.wallet = "".join(naccount.wallet)

    db_create()
    
    list = os.listdir(path)
    number_of_files = len(list)
        
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        sql = f"""INSERT INTO users(id, wallet, cash, amount_of_money )
        VALUES ({i}, '{naccount.wallet}', {naccount.cash}, {naccount.aom});"""
        cursor = conn.cursor()
        cursor.execute(sql)
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
        sql = f"""INSERT INTO users(amount_of_money )
        VALUES ({amount});"""
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

def gcash_update(gonderen, miktar):
    list = os.listdir(path)
    number_of_files = len(list)
    
        
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        c = conn.cursor()
        newcash = c.execute(f'''SELECT cash FROM users WHERE "wallet = {gonderen}"''')
        sql = f"""INSERT INTO users(cash) WHERE wallet = {gonderen}
        VALUES ({newcash - miktar});"""
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
def acash_update(alan, miktar):
    list = os.listdir(path)
    number_of_files = len(list)
    
        
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        c = conn.cursor()
        newcash = c.execute(f'''SELECT cash FROM users WHERE "wallet = {alan}"''')
        sql = f"""INSERT INTO users(cash) WHERE wallet = {alan}
        VALUES ({newcash + miktar});"""
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
        




def signin():
    
    userwallet = input("Wallet adresinizi giriniz: ")
   
    list = os.listdir(path)
    number_of_files = len(list)  
    wallets = []
    for i in range(1,number_of_files + 1):
        conn = sqlite3.connect(f"{path}/user{i}.db")
        c = conn.cursor()
        wallet = c.execute(f'''SELECT wallet FROM users''')
        wallets.append(wallet)
    
    for row in wallets:
        
        if userwallet == row:
            print("Basariyla giris yaptiniz.")
            currentuser = userwallet
        else:
            print("Kullanici bulunamadi.")
            break
    
    
    # def shasher(hash):
    #     thash = '
    #     i = 0
    #     hash += hash
    #     while len(thash) < 23:
    #         thash += hash[i]
            
    #         i += 2
    #     return thash
        
        
    # def hasher(gwallet, awallet, miktar):
    #     hash = ''
    #     i = 0
    #     k = 0
    #     smiktar = str(miktar)
    #     limit = min(len(gwallet),len(awallet))
    #     while len(hash) < 21:
    #         hash += gwallet[i] + awallet[i] + str(((int(smiktar[k]) + i)*9) %10)
    #         i += 1
    #         k += 1
            
    #         if i == limit:
    #             i = 0
    #         if k == len(str(smiktar)):
    #             k = 0
    #     return shasher(hash)
    





        
    def sendcoin():
        gonderen = currentuser
        alan = input("Alicinin Wallet adresi: ")
        miktar = int(input("Miktar: "))
        amount_update(miktar)
        if verification:
            acash_update(alan, miktar)
            gcash_update(gonderen, miktar)
            
            
            print("Islem onaylandi")
        else:
            print("Islem onaylanamadi!!!")
            
    secim = input(f"{coinname} gondermek icin gonder yaziniz: ")
    
    if secim == 'gonder':
        sendcoin()
            
            
            
            
        
    
    
    
    


print(" "*20 + coinname)
   
up_or_in = input("Kayit olmak icin kayit, giris yapmak icin giris yaziniz: ")

if up_or_in == 'kayit':
     signup()

elif up_or_in == 'giris':
    signin()
    
    
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


        





