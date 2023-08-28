from random import randint
#Задача №17. Общее обсуждение
#Дан список чисел. Определите, сколько в нем
#встречается различных чисел.
#Input: [1, 1, 2, 0, -1, 3, 4, 4]
#Output: 6

list = [randint(-10,10) for _ in range(10)]

#for i in range(10):
#    list.append(randint(-10,10))

print(list)

result = set(list)

print(len(result))