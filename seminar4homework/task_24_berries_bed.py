"""задача 2 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата.
*Дополнительно
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов где это возможно
Используйте функции
"""
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

def collect_beries(berries_bed:list, brunch:int) -> int: #Собираем ягоды на грядке berries_bed с куста brunch
    l=len(berries_bed)
    #т.к. грядка круглая любой номер куста будет валиден
    #brunch %=len #делим по модулю 
    if l<=3: #0,1,2,3 куста в грядке. То есть грядка может быть пустой без кустов
        return sum(berries_bed)
    else: 
        return berries_bed[(brunch-1)%l]+ berries_bed[(brunch)%l]+ berries_bed[(brunch+1)%l] #Сумма трех кустов. Делим по модулю чтоб не было выхода за пределы
    return 0


berries=0
berries_bed=[]
while berries>=0:
    berries=try_input_int("Введите количество ягод на кусте. Для окончания ввода введите отрицательное число: ")
    if berries>=0:
        berries_bed.append(berries)
print(f"Наши ягодки подросли: {berries_bed}")
brunch_number=try_input_int("Введите номер куста: ",True)
brunch_number=brunch_number-1 #Предполагаем, что пользователь нумерует кусты с 1, а у нас массивы с 0
print(f"Колличество ягод собранных с {brunch_number+1} куста равно: {collect_beries(berries_bed,brunch_number)}")