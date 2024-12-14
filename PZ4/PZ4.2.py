def AddLeftDigit(D, K):
  return int(str(D) + str(K))

# Ввод данных
K = int(input("Введите целое число: "))
while type(K) != int:  # обработка исключений
    try:
        K = int(K)
    except ValueError:
        print("Неправильно ввели!")
        K = input("Введите первое число: ")

D1 = int(input("Введите первую цифру (1-9): "))

while type(D1) != int:  # обработка исключений
    try:
        D1 = int(D1)
    except ValueError:
        print("Неправильно ввели!")
        D1 = input("Введите первое число: ")

D2 = int(input("Введите вторую цифру (1-9): "))

while type(D2) != int:  # обработка исключений
    try:
        D2 = int(D2)
    except ValueError:
        print("Неправильно ввели!")
        D2 = input("Введите первое число: ")

# Добавляем первую цифру
K = AddLeftDigit(D1, K)
print("Результат добавления D1:", K)

# Добавляем вторую цифру
K = AddLeftDigit(D2, K)
print("Результат добавления D2:", K)