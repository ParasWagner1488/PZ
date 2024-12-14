def sit(P):
  deposit = 1000
  m = 0
  while deposit < 1100:
    deposit += deposit * P / 100
    m += 1

  return m, deposit

x = input("Введите процентную ставку вклада: ")
while type(x) != float:  # обработка исключений
    try:
        x = float(x)
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите первое число: ")
K, S = sit(x)

print(f"Количество месяцов: {K}")
print(f"Итоговый депозит состовляет: {S:.2f}")