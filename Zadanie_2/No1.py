#Выполнил:Букин Илья 301818
#Задача 1:Создать список и заполнить его элементами различных типов данных.
#Реализовать скрипт проверки типа данных каждого элемента. 
#Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
var_str = "Проверка типов с помощью функции Type()"
var_float = 64.324
var_list = [20, 15, 14, 33, 12]
var_tuple = (8, 65, 45, 87, 37, 737, 645)
var_dict = {"а": 11, "б": 22, "в": 33}
var_set = {"а", "б", "в", "г"}

list = [var_str, var_float, var_list, var_tuple, var_dict, var_set]
for i in list:
    print(f'{i} is {type(i)}')