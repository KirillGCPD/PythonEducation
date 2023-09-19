from time import time

def how_long(func):
    start = time()
    func()
    print(f"На это ушло {time()-start} секунд")

def create_list():
    return [i for i in range(50000)]

sp =[1,2,3,4,5]

def item(x):
    return x^2 if x>0 else -x

print(item(5))