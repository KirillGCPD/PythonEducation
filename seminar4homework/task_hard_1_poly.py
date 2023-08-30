
from random import randint
"""
пользователь вводит натуральное число K. 
Задача - сформировать многочлен степени K, 
где каждый коэффициент случайный от 0 до 10

например, пользователь ввел 3

на выходе может получиться 3*x^3 + x + 9 = 0
"""
def try_input_int(message:str, no_negative:bool=False)->int: #приглашение на ввод числа. nonnegative true если требуется не отрицательное число
    number=0
    while True:
        try:
            number=int(input(message))
            if no_negative and number<0: #Если стоит флаг no_negative и число отрицательное
                raise Exception('Negative') #вызываем исключение с текстом "Negative"
            break
        except Exception as e:
            if str(e)=="Negative": #Если текст исключения содержит негатив то выведем об этом предупреждение
                print("Вы ввели отрицательное число")
            else:
                print("Вы ввели не целочисленное число")
    return number

def k_to_str(k:int,first:bool=False,last:bool=False)->str:
    if k==0:
        return ""
    elif k==1:
        if first:
            return ""
        elif last:
            return f"+{k}"
        else:
            return "+"
    elif k==-1:
        if last:
            return f"{k}"
        else:
            return "-"
    elif k>1:
        if first:
            return f"{k}"
        else:
            return f"+{k}"
    elif k<1:
        return f"{k}"
def k_to_pow(k:int)->str:
    if k==1:
        return "x"
    elif k>1:
        return f"x^{k}"
    elif k==0:
        return f""
def trim_poly(poly_list:list)->str: #обрезать многочлен от 0
    copy=poly_list.copy()
    for i in poly_list:
        if i==0:
            copy.pop(0)
        else:
            break
    return copy

def poly_to_str(poly_list:list)->str:
    poly_list=trim_poly(poly_list)
    print(poly_list)
    #print(poly_list)
    #print(trim_poly(poly_list))
    str=""
    k=len(poly_list)
   
    for i in range(k):
        r=poly_list[i]
       
        if r!=0:
            if i==0:
                str += f"{k_to_str(r,True)}{k_to_pow(k-i-1)}"
            elif i==k-1: #
                str += f"{k_to_str(r,first,True)}"
            elif k-i-1==1: #last
                str += f"{k_to_str(r,first)}x"
            elif i!=0 and i!=k-1: # middle
                str += f"{k_to_str(r,first)}{k_to_pow(k-i-1)}"
        first=False

    str+="=0"
    return str

#list = [randint(-10,10) for _ in range(10)]
#k=int(input("Введите натуральное число: "))

#k=try_input_int("Введите степень многочлена K: ", True)

print(poly_to_str([-2]))
print(poly_to_str([-2,-2]))
print(poly_to_str([-2,-2,-2]))
print(poly_to_str([2,2,2,2]))

"""
for i in range(10):
    poly = [randint(-2,2) for _ in range(k)]
    str =poly_to_str(poly)
    print(poly)
    print(str)"""