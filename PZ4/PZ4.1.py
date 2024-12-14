def c(number):
  count = 0
  while number > 0:
    count += 1
    number -= sum(int(digit) for digit in str(number))
  return count

number = input("Введите число: ")
while type(number) != int:  # обработка исключений
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите первое число: ")

oper = c(number)

print(f"Для числа {number} потребуется {oper} операция(ий).")