#Выпoлнил:Букин Илья 301818
#Задача 5:Запросите у пользователя значения выручки и издержек фирмы.
#Oпределите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
viruchka = int(input("Введите значение выручки: "))
izderzhki = int(input("Введите значение издержек: "))
if viruchka > izderzhki:
    pribil = viruchka-izderzhki
    rentabelnost = pribil/viruchka
    Kolichestvo_rabotnikov = int(input("Сколько работников у вас в подчинении: "))
    zarplata_rabotnika = pribil/Kolichestvo_rabotnikov
    print(f"Конгратулейшен,май бизинесс фриенд. Вы иметь целых {pribil} единиц чистой прибыль")
    print(f"Ваш подчиненный получать целый {pribil/Kolichestvo_rabotnikov} единиц на одного работника")
    print(f"Партия Китая гордится тобой. Вы получить плюс второй миска рис. Да здравствует капитализм!")

if viruchka < izderzhki:
    pribil = viruchka-izderzhki
    rentabelnost = pribil/viruchka
    Kolichestvo_rabotnikov = int(input("Сколько работников у вас в подчинении: "))
    zarplata_rabotnika = pribil/Kolichestvo_rabotnikov
    print(f"Это не вери бьютифул. Вы иметь {pribil} единиц прибыль.")
    print(f"Ваш подчиненный голодать из-за вас, так как получать {pribil/Kolichestvo_rabotnikov} единиц на одного работника")
    print(f"Партия Китая недовольна. Вы плохо работать и приговорены к расстрелу!")