from decimal import Decimal
#Задача 1 HARD по желанию Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
#456 -> 3
#0 -> 1
#89,126 -> 5
#0,001->4

def digit_count(dec): # Основная функция, возвращает количество цифр в числе
    dec=abs(dec)  #Сделаем число положительным
    if dec==0: #если 0 то сразу результат
        return 1
    intpart=int(dec) #Целая часть
    floatpart=dec-int(dec) #Дробная часть
    count=intdigit_count(intpart) #Количество цифр для целой части
    if floatpart < 1 and floatpart>0:
        while floatpart-int(floatpart)!=0: #это разница между целой и дробной частью, мы будем домножать дробную пока не останутся знаки после запятой
            floatpart=floatpart*10
            count+=1
    return count

def intdigit_count(intnumber): #Количество цифр в целом числе
    count=0
    if intnumber==0:
        return 1
    while intnumber!=0:
        count+=1
        intnumber//=10
    return count

dec=0
while True: #В данном случае условие выхода - число больше 0. Альтернативный вариант break после ввода
    try:
        dec=Decimal(input("Введите число N больше 0 для вывода степеней двойки:"))
        break #Цикл будет повторятся, пока пользователь не введет корректно число
    except:
        print("Кажется вы ввели не число, повторите попытку")

print(digit_count(dec))
