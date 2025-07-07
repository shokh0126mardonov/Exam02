from sys import exit

def deposit(balance, amount):
    summa = balance + amount
    return summa

def withdraw(balance, amount): 
        return balance - amount
   
def check_balance(balance):
    return balance

balance = 0
while True:
    print("===== Menu =====")
    print("1.Pul qo'shish")
    print("2.Pul yechish")
    print("3.check")
    print("4.Exit")
    
    tanlov = int(input('tanlovni kiriting : '))
    
    if tanlov == 1:
       
        amount = float(input("qancha pul qo'shmoqchisiz : "))
        deposit(balance,amount)
        balance = deposit(balance,amount)
        print('deposit yangilandi')
        
    elif tanlov == 2:
        amount = float(input("Qancha pul yechmoqchisiz : "))
        if balance >= amount:
            withdraw(balance,amount)
            print("Balans yangilandi")
            balance = withdraw(balance,amount)
        else:
            print("oldin depozit qiling yoki balansizngizdan ko'p summa yechmoqchi bo'yabsiz")
        
    elif tanlov == 3:
        print(check_balance(balance))
        
    elif tanlov == 4:
        exit()