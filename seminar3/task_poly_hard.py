
from random import randint
"""
Даны два многочлена, которые вводит пользователь.
Задача - сформировать многочлен, содержащий сумму многочленов.
Степени многочленов могут быть разные.
например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re
"""
str1="        2x^2 + 4x + 5 = 0"
str2="5x^3 - 3*x^2     - 12 = 0"
r1=[0,2,4,5]
r2=[5,-3,0,-12]
r3=[5,-1,4,-7]

def parsePoly(str):
    return [0]

def printPoly(polyList):
    return "5x^3 - 3*x^2     - 12 = 0"

def sumPoly(polyList1,PolyList2):
    return [0]