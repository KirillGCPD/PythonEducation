"""
задача 3 необязательная.
Даны два многочлена, которые вводит пользователь. как две строки.
Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

Степени многочленов могут быть разные.

например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re"""
#################################################################
########   ОБЛАСТЬ ПАРСИНГА МНОГОЧЛЕНА ##########################
#################################################################
#Функция для парсинга входного выражения.
#Регулярные выражения не используются. Идет последовательный разбор символов
def parse_poly(poly:str)->list:
    poly=poly.replace(" ","") #Для удобства убираю пробелы
    sign = True #Знак текущего члена
    first= True #Если это первый
    current_k_str="" #собираем строку для коэффициента
    current_k=0 #в конце строка преобразуется в int
    current_pow_str="" #собираем строку для степени (поддерживаются многозначные степени)
    current_pow=0 #в итоге степень это число
    pow_parse_mode=False #False -разбирам коэффициент True -разбираем степень
    dict_res=dict() #в словарь запишем значения коэффициентов для степеней
    digits={"0","1","2","3","4","5","6","7","8","9"} #проверка символа на цифру
    for el in poly: #последовательно по многочлену
        if el in digits: #если символ число
            if pow_parse_mode: #мы в режиме степени
                current_pow_str+=el #добавляем цифру в строку степени
            else:
                current_k_str+=el #добавляем цифру в строку коэффициента
        if el=="x": #встретили x включили режим парсинга степени
            pow_parse_mode=True #режим степени
            current_pow=1 #на всякий случай - у нас уже есть степень =1 на случай если дальше не будет домика ^
            current_k=1
        #if el=="^": #встретили ^ 
            #pow_parse_mode=True
        if el=="-" or el=="+" or el=="=": #встретили знак перехода на следующий элемент
            if first: #при этом если это самое начало
                sign = el!="-" #просто запишем знак в sign (true + false -)
            else:
                if current_k_str!="": #если строка коэффициента не пустая
                    current_k=int(current_k_str) #парсим то что накопили
                if current_pow_str!="":  #если строка степени не пустая
                    current_pow=int(current_pow_str) #так же парсим
                if sign: #если знак +
                    if current_pow in dict_res: #тут идет проверка на случай если данная степень в многочлене встретится дважды
                        dict_res[current_pow]+=current_k #если уже была, то мы их складываем тем самым x+x=0 првератится в 2x=0
                    else:
                        dict_res[current_pow]=current_k
                else: #знак минус то же самое:
                    if current_pow in dict_res:
                        dict_res[current_pow]-=current_k
                    else:
                        dict_res[current_pow]=-current_k
                pow_parse_mode=False #обнуляем набор текущего
                current_pow_str=""
                current_k_str=""
                current_pow=0
                sign = el!="-"
        first=False #срзау после первого элемента 
    keys=list(dict_res) #достали ключи
    max_key=max(keys) #максимальный ключ - степень многочлена
    result=[0 for _ in range(max_key+1)] #создали массив для членов
    for key in keys: #для каждого ключа
        result[max_key-key]=dict_res[key]  #записали коэффеициенты    
    
    return result

#################################################################
########   Суммируем многочлены      #############################
#################################################################
def poly_sum(poly1:list,poly2:list)->list:
    m=len(poly1)
    n=len(poly2)
    max=n
    if m>n:
        max=m
    result=[0 for _ in range(max)] #заполняем 0 сумму
    
    for index, value in enumerate(poly1):
        result[index+max-m]=value
    for index, value in enumerate(poly2):
        result[index+max-n]+=value
    return result

#################################################################
########   ОБЛАСТЬ ВЫВОДА МНОГОЧЛЕНА#############################
#################################################################
def k_to_str(k:int,first:bool=False,last:bool=False)->str: #вспомогательная - коэффициент в строку
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
def k_to_pow(k:int)->str: #вспомогаельное - формируем степень
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

#################################
######ТЕЛО ПРОГРАММЫ#############
#################################
str1=""
str2=""
poly1=list()
poly2=list()
while True:
    try:
        str1=input("Введите многочлен №1: ")
        poly1=parse_poly(str1)
        break
    except:
        print("Мы не смогли распарсить многолчен, повторите попытку")
while True:
    try:
        str2=input("Введите многочлен №2: ")
        poly2=parse_poly(str2)
        break
    except:
        print("Мы не смогли распарсить многолчен, повторите попытку")
print(f"Вы ввели многочлены: {poly_to_str(poly1)} и {poly_to_str(poly2)}")
sum=poly_sum(poly1,poly2)
print(f"Их сумма равна: {poly_to_str(sum)}")