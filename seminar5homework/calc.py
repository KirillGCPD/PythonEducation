
#Вспомогательная функция убирает лишние скобки (( () () (()) ) ) ->() () (())
def remove_brackets(expression:str)->str:
    if expression[0]!="(": #если в начале скобки нет, убирать не нужно
        return expression
    brackets=0 #вложенность
    for i,v in enumerate(expression):
        if v=="(":
            brackets+=1
        if v==")":
            brackets-=1
            if i!=len(expression)-1 and brackets==0: #вложенность окончена, а у нас не последний элемент, значит это было выражение вида: "((1+1)+1)+1"
                return expression
            else: #Вложенность закончена на последнем элементе, значит это лишняя скобка
                return remove_brackets(expression[1:-1]) #отрезаем края и повторяем рекурсивно, вдруг там пара скобок (((2+2))) -> 2+2
    return expression    

#Основной метод разбора
def calc_exp(expression:str):
    expression=expression.replace(" ","") #Удалю пробелы если есть
    expression=remove_brackets(expression) #Убираю лишние скобки
    depth=0 #глубина вложенности
    left_str="" #левая часть
    right_str="" #правая часть
    operators = "+-" #сначала будем делить на левую правую по знакам сложения и вычитания 2*3 - 3*3   =  [2*3]  - [3*3]
    operators2="*/"
    i=len(expression)-1
    while i>0: #Цикл по выражению с конца. Если искать с начала, то выражения вроде 1/2*3 будут разбиваться на (1) / (2*3) вместо (1/2) * 3  
        el=expression[i] #текущий элемент
        if el==")": 
            depth+=1 #если у нас скобочка увеличиваем вложенность
        if el=="(":
            depth-=1 #если нет уменьшаем
        if el in operators and depth==0: #У нас есть оператор, если мы не в скобочках, то на нем можно резать строку
            left_str=expression[:i]
            right_str=expression[i+1:]
            if el=="+":    
                return calc_exp(left_str)+calc_exp(right_str)
            elif el=="-":
                return calc_exp(left_str)-calc_exp(right_str)
        i-=1
    depth=0
    i=len(expression)-1
    while i>0: #то же самое для умножения и деления
        el=expression[i]
        if el==")":
            depth+=1
        if el=="(":
            depth-=1
        if el in operators2 and depth==0:
            left_str=expression[:i]
            right_str=expression[i+1:]
            if el=="*":
                return calc_exp(left_str)*calc_exp(right_str)
            elif el=="/": 
                return calc_exp(left_str)/calc_exp(right_str)
        i-=1
    #print(f"end: {expression}")
    return float(expression)
   
#набор тестов ("Выражение", Ожидаемый результат)
test_exp=[("-(1+2)/(-3+1)+(1/2*3)",0),
     ("(1+2)/(3+1)+4-(1/2*3)",3.25),
     ("(1+2)/(3+1)/(1/2*3)",0.5),
     ("(1+2)/(33*34/3)*(3+1)+(1/2*3/4+1)",1.40708),
     ("1+2/(3+1)+(1/2.3*3)",2.8043),
     ("(1+2)/3+1+1/2*3",3.5),
     ("(1+2)/(3+1)+(1/2*3)",2.25),
     ("1+2/(3+1)+1/2*3",3)
     ]

for test_case in test_exp:
    result=calc_exp(test_case[0])
    success=abs(result-test_case[1])<0.0001
    print(f"Выражение: {test_case[0]}. Ожидание: {test_case[1]}. Результат: {result}. Верно: {success}")