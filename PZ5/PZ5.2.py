n = int(input("Введите размер списка A (N < 15): "))

while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите первое число: ")

a = []
print("Введите элементы списка A:")
for i in range(n):
    a.append(int(input()))


b = []
for i in range(n):
    if (i + 1) % 3 == 0:
        b.append(a[i])


print("Размер списка B:", len(b))


print("Элементы списка B:", b)