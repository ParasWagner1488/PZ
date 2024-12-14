def find(A):
    max = None
    for i in range(1, len(A), 2):
        if max is None or A[i] > max:
            max = A[i]
    return max

num = []
while True:
    A = input('Введите числа (q = Выход): ')
    if A == 'q':
        break
    try:
        num.append(int(A))
    except ValueError:
        print("Некорректный ввод. Введите число.")

max = find(num)
if max is not None:
    print(f"Максимальный элемент с нечетными номерами: {max}")
else:
    print("В списке нет элементов с нечетными номерами.")