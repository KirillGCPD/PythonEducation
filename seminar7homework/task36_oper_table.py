"""Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**"""

#С единицы начинаем на случай если операция будет с делением
def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1,num_rows+1):
        for y in range(1,num_columns+1):
            print(f"{operation(x,y)}",end="\t")
        print(end="\n")

print(f"Операция умножения *: ")
print_operation_table(lambda x, y: x * y)
print(f"Нарисовать треугольник из плсюв через лямпду")
print_operation_table(lambda x, y: "+" if x >= y else "-")