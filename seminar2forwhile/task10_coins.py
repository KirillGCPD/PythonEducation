import random
#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

#Списки не использую осознанно
n = 10 #Количество монеток
headsnumber = 0 #Количество орлов

for i in range(n): #Бросаем моентки
    coin=bool(random.randint(0,2)) #0 - false 1 - true
    if coin:
        print(f"[Орел]",end=" ")
        headsnumber +=1 #считаем орлов
    else:
        print("[Решка]",end=" ")

print("",end="\n")
if (headsnumber>n/2):
    print(f"Нужно перевернуть {n-headsnumber} монет")
else:
    print(f"Нужно перевернуть {headsnumber} монет",end="\n")