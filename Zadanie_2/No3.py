#Выполнил:Букин Илья 301818
#Задача 3:Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
a = int(input ('Введите номер месяца (от 1 до 12) '))
if a == 12 or a == 1 or a == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif a == 3 or a == 4 or a == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif a == 6 or a == 7 or a == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif a == 9 or a == 10 or a == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])