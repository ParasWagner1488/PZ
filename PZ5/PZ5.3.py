def list(lst):
  n = len(lst)
  sh = [0] * n
  sh[0] = 0
  for i in range(1, n):
    sh[i] = lst[i - 1]
  return sh


lst = [1, 2, 3, 4, 5]

shift = list(lst)

print(f"Исходный список: {lst}")

print(f"Сдвинутый список: {shift}")