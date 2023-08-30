"""
задача 3 необязательная.
Даны два многочлена, которые вводит пользователь. как две строки.
Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

Степени многочленов могут быть разные.

например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re"""


def parse_poly(poly:str)->list:
    #2x^2+4x+5=0
    current_k_str=""
    current_k=0
    current_pow_str=""
    current_pow=0
    pow_parse_mode=False
    digits={"0","1","2","3","4","5","6","7","8","9"}
    for el in poly:
        if el in digits:
            if pow_parse_mode: #парсим степень
                current_pow_str+=el
            else:
                current_k_str+=el
        if el=="x": #встретили x включили режим парсинга степени
            pow_parse_mode=True
            current_pow=1
        if el=="^":
            pow_parse_mode=True
    return


str="2x^2 + 4x + 5 = 0"
str=str.replace(" ", "")
print(str)