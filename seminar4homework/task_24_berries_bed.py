"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.
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
#####################
##Ищем лучший куст###
#####################
def maximize_beries(berries_bed:list) -> (int,int): #Не сразу прочитал услвие задачи, сначала просто задавал ответ на любом кусте.
    current=0                                        #Для поиска лучшего добавлен этот метот, который использует предыдущий
    max_berries=0
    for index,branch in enumerate(berries_bed):
        berries=collect_beries(berries_bed,index)
        if berries>max_berries:
            current=index
            max_berries=berries
    return (max_berries,current)

berries=0
berries_bed=[]
while berries>=0:
    berries=try_input_int("Введите количество ягод на кусте. Для окончания ввода введите отрицательное число: ")
    if berries>=0:
        berries_bed.append(berries)
print(f"Наши ягодки подросли: {berries_bed}")
print(f"Произвожу анализ: ")
typle_res=maximize_beries(berries_bed)
print(f"Мы пришли к выводу, что лучше начать сбор с куста номер {typle_res[1]+1} на котором мы получим {typle_res[0]} ягод")
