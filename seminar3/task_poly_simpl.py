
from random import randint
"""
пользователь вводит натуральное число K. 
Задача - сформировать многочлен степени K, 
где каждый коэффициент случайный от 0 до 10

например, пользователь ввел 3

на выходе может получиться 3*x^3 + x + 9 = 0
"""
list = [randint(-10,10) for _ in range(10)]
#k=int(input("Введите натуральное число: "))
k=3
str =""
for i in range(k):
    r=randint(-10,10)
    if i==0:
        str += f"{r}x^{k-i-1} "
    if i==k-1: #
        if r>0:
            str += f"+ {r} ="
        else:
            str += f"{r} ="
    if i!=0 and i!=k-1: # middle
        if r>0:
            str += f"+{r}x^{k-i-1} "
        else:
            str += f"{r}x^{k-i-1} "
        
str+=" 0"

print(str)