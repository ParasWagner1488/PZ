"""Вариант 27
Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить его в новый текстовый файл."""


# Простое чтение и запись блока
with open('Dostoevsky.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Извлекаем часть с 1857 годом (простой вариант)
start = text.find('1857')
if start != -1:
    with open('new_file.txt', 'w', encoding='utf-8') as f:
        f.write(text[start:])
    print("Блок 1857 года сохранен")
else:
    print("1857 год не найден в тексте")

