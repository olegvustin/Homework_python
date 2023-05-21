"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
name = input("Введите Ваше имя:")
password = input("Введите Ваш пароль:")
age = input("Введите Ваш  возраст:")
print(f"Ваши данные для входа в аккаунт: имя - {name}, пароль - {password}, возраст - {age}")

"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600

"""
s = input("Введите время в секундах: ")

s = int(s)
h = float(s/3600)
h = round(h,2)
m = float(s/60)
m = round(m,2)
print(f"Время в формате ч:м:с - {h} : {m} : {s}")

"""Второй вариант решения:
 исходя из логики 3650 секунд - это 1 час: 00 минут: 50 секунд"""

time = int(input("Второй вариант.Введите время в секундах: "))

hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = (time - hours * 3600) - minutes * 60
print(f'{hours}:{minutes}:{seconds}')

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите целое положительное число: "))
print(n + int(str(n) * 2) + int(str(n) * 3))

"""
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""
revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
staff = int(input('Введите численность сотрудников фирмы: '))
bacon = revenue - costs
if bacon == 0: print('Выручка равна издержкам')
elif revenue > costs:
    print(f'Прибыль в этом месяце составила: {bacon}')
    profit = bacon/revenue
    print(f'Рентабельность выручки составила: {profit}')
    bacon_staff = float(bacon/staff)
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет = {bacon_staff}')
else:
    print('Организация убыточна')