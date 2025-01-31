'''Вариант 28
1. Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S
вставить строку S0.
2. Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
расположенную между первым и последним пробелом исходной строки. Если
строка содержит только один пробел, то вывести пустую строку'''


def task1(c, s, s0):
  result = []
  for i in range(len(s)):
    if s[i] == c:
      result.append(s0)
    result.append(s[i])
  return ''.join(result)

def task2(string):
  spaces = [i for i, char in enumerate(string) if char == ' ']
  if len(spaces) == 1:
    return ''
  elif len(spaces) > 1:
    return string[spaces[0] + 1:spaces[-1]]
  else:
    return ''