"""Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21"""

#0 1 1 2 3 5

def simple(number,current):
    if number%current ==0 and current!=1:
        return False
    else:
         if current==1:
            return True
         else:
            return simple(number,current-1)

number=7
print(simple(number,number-1))

