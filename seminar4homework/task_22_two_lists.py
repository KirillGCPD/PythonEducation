#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого 
#множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def try_input_int(message, no_negative=False): #приглашение на ввод числа. nonnegative true если требуется не отрицательное число
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

def union_with_no_repeats(list1:list,list2:list)->list:
    list1.extend(list2)
    remove_repeats = set(list1)
    result=list(remove_repeats)
    result.sort()
    return result

n=try_input_int("Введите количество элементов первого списка n: ", True)
m=try_input_int("Введите количество элементов второго списка m: ", True)
list1=[]
list2=[]
for i in range(n):
    list1.append(try_input_int(f"Введите {i} элемент первого списка: ",False))
for i in range(m):
    list2.append(try_input_int(f"Введите {i} элемент второго списка: ",False))


result = union_with_no_repeats(list1,list2)

print(result)