from random import randint
from time import time

def list_gen(min=-5,max=5,length=10000000):
    return [randint(min,max) for i in range(length)]

my_list=list_gen()

def algo_time(func,x):
    start = time()
    func(x)
    end = time() - start
    print(f"Выполнено за {end} секунд")

def make_heap(list,len,root):
    largest=root
    left=2*root+1
    right=2*root+2

    if left<len and list[root]<list[left]:
        largest=left
    if right<len and list[largest] < list[right]:
        largest=right

    if largest != root:
        (list[root], list[largest]) = ( list[largest] , list[root]) 
        make_heap(list, len, largest)

def heap_sort(list):
    for i in range(len(list)//2,-1,-1):
        make_heap(list,len(list),i)
    for i in range(len(list)-1,0,-1):
        (list[i],list[0])=(list[0],list[i])
        make_heap(list,i,0)

#print(my_list)
algo_time(heap_sort,my_list)
#print(my_list)