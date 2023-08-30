"""задача 2 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата.
*Дополнительно
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов где это возможно
Используйте функции
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

def ord_to_char(number:int)->str: #преобразуем число в цифру 1->1 2->2 но 10->A 11->B и т.д.
    if number<10:
        return str(number)
    else:
        return str(chr(ord('a')+number-10)) #ord- возвращает номер символа в A в ASCII далее к нему мы смещаемся правее если число больше 10
    
def int_to_number_system(number:int,base_number:int) ->str:
    result=""
    while number//base_number!=0:     
        result=ord_to_char(number%base_number)+result
        number //=base_number
    result=ord_to_char(number%base_number)+result
    if base_number==2: #добавляем приставку, если основание не равно 2, 8 или 16 то число будет без преффикса
        result="0b"+result
    elif base_number==8:
        result="0o"+result
    elif base_number==16:
        result="0x"+result
    return result

number=try_input_int("Введите число: ",True)
print(f"BIN представление: {int_to_number_system(number,2)}. Проверка функцией bin: {bin(number)}")
print(f"OCT представление: {int_to_number_system(number,8)} Проверка функцией oct: {oct(number)}")
print(f"HEX представление: {int_to_number_system(number,16)} Проверка функцией hex: {hex(number)}")