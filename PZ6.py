'''Вариант 27  '''

import math
import random

'''1. Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами: \( A_2, A_4, A_6, \ldots \).'''

# Задание 1
def task1():
    print("Задание 1:")
    A = [random.randint(1, 100) for _ in range(10)]
    print(f"Список A: {A}")
    
    min_even = min(A[i] for i in range(1, len(A), 2))
    print(f"Минимальный элемент с четными номерами: {min_even}")

'''2. Дан целочисленный список A размера N. Переписать в новый целочисленный список 
B все четные числа из исходного списка (в том же порядке) и вывести размер полученного список B и его содержимое.  '''

# Задание 2
def task2():
    print("\nЗадание 2:")
    A = [random.randint(1, 50) for _ in range(8)]
    print(f"Исходный список A: {A}")
    
    B = [x for x in A if x % 2 == 0]
    print(f"Список B (четные): {B}")
    print(f"Размер списка B: {len(B)}")

'''3. Дано множество A из N точек (\( N > 2 \), точки заданы своими координатами x, y).
Найти наибольший периметр треугольника, вершины которого принадлежат различным точкам множества A
, и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при задании множества A). '''

# Задание 3
def task3():
    print("\nЗадание 3:")
    N = 6
    X = [random.randint(-10, 10) for _ in range(N)]
    Y = [random.randint(-10, 10) for _ in range(N)]
    
    print(f"Точки:")
    for i in range(N):
        print(f"  Точка {i+1}: ({X[i]}, {Y[i]})")
    
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    max_perimeter = 0
    best_points = []
    
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                a = distance(X[i], Y[i], X[j], Y[j])
                b = distance(X[j], Y[j], X[k], Y[k])
                c = distance(X[k], Y[k], X[i], Y[i])
                perimeter = a + b + c
                
                if perimeter > max_perimeter:
                    max_perimeter = perimeter
                    best_points = [(X[i], Y[i]), (X[j], Y[j]), (X[k], Y[k])]
    
    print(f"Наибольший периметр: {max_perimeter:.2f}")
    print("Вершины треугольника:")
    for point in best_points:
        print(f"  ({point[0]}, {point[1]})")

# Запуск всех заданий
task1()
task2()
task3()
