# Исходная матрица
m = [[1, 6, -3], [9, -12, 15], [0, 18, 21]]

# Задача 1
good_nums = []
for row in m:
    for num in row:
        if num > 0 and num % 3 == 0:
            good_nums.append(num)
print("Среднее:", sum(good_nums) / len(good_nums))

# Задача 2
n = int(input("Строка: "))
m[n] = [x+3 for x in m[n]]
print("Новая матрица:", m)
