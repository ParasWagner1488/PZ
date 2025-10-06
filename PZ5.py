
'''Вариант 27
1. Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.'''

import random

# Задание 1
def generate_and_check():
    num = random.randint(1000, 9999)
    digits = str(num)
    has_duplicates = len(set(digits)) != len(digits)
    return num, has_duplicates

print("Задание 1:")
number, result = generate_and_check()
print(f"Сгенерированное число: {number}")
print(f"Есть одинаковые цифры: {result}")

'''2. Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K справа цифру D 
(D — входной параметр целого типа, лежащий в диапазоне 0-9, K — параметр целого типа, являющийся одновременно входным и выходным).
С помощью этой функции последовательно добавить к данному числу K справа данные цифры D1 и D2, выводя результат каждого добавления.'''


# Задание 2
def AddRightDigit(D, K):
    return K * 10 + D

print("\nЗадание 2:")
try:
    K = int(input("Введите число K: "))
    D1 = int(input("Введите цифру D1 (0-9): "))
    D2 = int(input("Введите цифру D2 (0-9): "))
    
    if K <= 0 or D1 < 0 or D1 > 9 or D2 < 0 or D2 > 9:
        print("Ошибка: K должно быть положительным, D1 и D2 в диапазоне 0-9")
    else:
        print(f"Исходное число K: {K}")
        
        K = AddRightDigit(D1, K)
        print(f"После добавления D1={D1}: {K}")
        
        K = AddRightDigit(D2, K)
        print(f"После добавления D2={D2}: {K}")
        
except ValueError:
    print("Ошибка ввода! Введите целые числа.")
