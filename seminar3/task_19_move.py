from random import randint
#Задача №19. Решение в группах
#Дана последовательность из N целых чисел и число
#K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K –
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]

list = [randint(-10,10) for _ in range(10)]
l=len(list)
k=3
print(list)
result=[]

for i in range(l):
    index=i-k
    if index>=l:
        index=index-l
    print(index)
    result.append(list[index])
print(result)

for i in range(k):
     list.insert(0,list.pop())
print(list)