#Выполнил:Букин Илья 301818
#Задача 6:Спортсмен занимается ежедневными пробежками. 
# В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
# Требуется определить номер дня, на который общий результат спортсмена составил не менее b километров. 
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = float(input("Сколько километров ты сегодня набегал,лентяй?: "))
b = float(input("А скока нада (в км)?:  "))
days = 1
if a > b:
    print(days)
while a < b:
    a = a + a/10
    days += 1
print(f'Каждый раз увеличивая результат на 10% ты достигнешь результата на {days} день')