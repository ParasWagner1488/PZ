'''1.Задание
Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
лежит в первой или третьей координатной четверти».'''

x = (input('Введите первую координату X: '))
y = (input('Введите первую координату Y: '))
while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите первое число: ")

while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print("Неправильно ввели!")
        y = input("Введите второе число: ")


def koord(x, y):
    if x < 0 and y > 0:
        print('Первая четверть')
    elif x > 0 and y > 0:
        print('Вторая четверть')
    elif x > 0 and y < 0:
        print('Третья четверть')
    elif x < 0 and y < 0:
        print('Четвёртая четверть')


result = koord(x, y)
print(result)