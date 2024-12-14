#Вариант Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
a = (input("Введите целое число > 0: "))

while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")


def sum(a):
    total = 0
    for i in range(a, 2 * a + 1):
        total += i ** 2
    return total

# Пример использования:
if a > 0:
    result = sum(a)
    print("Сумма:", result)
else:
    print("Пожалуйста, введите число больше 0.")