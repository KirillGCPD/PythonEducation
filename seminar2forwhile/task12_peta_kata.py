import random
#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# X+Y=S   X*Y=P 
X=random.randint(1,1000)
Y=random.randint(1,1000)
S=X+Y # Сумма  
P=X*Y # Произведение
count=0 #колличество попыток
solutionFound=False #для выхода

for xg in range(1,1001):
    for yg in range(1,1001):
        count+=1
        if xg+yg==S and xg*yg==P:
            print(f"Ура! Мы подобрали числа за {count} попыток. Это {xg} и {yg}. А Петя загадал: {X} и {Y}")
            solutionFound=True
            break
    if (solutionFound):
        break