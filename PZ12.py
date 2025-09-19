# Задача 1 - в одну строку
nums = [2, -3, 4, -1, 5, -2, 7, 8]
result = 1
for x in nums[:len(nums)//2]:
    if x < 0: result *= x
print("Произведение:", result)

# Задача 2 - генератор
def to_upper(s):
    yield from (c.upper() for c in s)

print("Результат:", ''.join(to_upper("hello")))
