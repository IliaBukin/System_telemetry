#Выполнил:Букин Илья 301818
#Задача 2:Для списка реализовать обмен значений соседних элементов, 
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().
var_list = input("Введите элементы списка: ").split()

for i in range(0, len(var_list)-1, 2):
    var_list[i], var_list[i+1] = var_list[i+1], var_list[i]

print(var_list)