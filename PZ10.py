# Определяем коллекции книг в каждом магазине
magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domknigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

# Ищем магазины с книгами Маяковского
magaziny_s_mayakovskim = []

if 'Маяковский' in magistr:
    magaziny_s_mayakovskim.append('Магистр')
if 'Маяковский' in domknigi:
    magaziny_s_mayakovskim.append('ДомКниги')
if 'Маяковский' in bukmarket:
    magaziny_s_mayakovskim.append('БукМаркет')
if 'Маяковский' in galereya:
    magaziny_s_mayakovskim.append('Галерея')

# Выводим результат
print("Книги Маяковского можно приобрести в следующих магазинах:")
if magaziny_s_mayakovskim:
    for magazin in magaziny_s_mayakovskim:
        print(f"- {magazin}")
else:
    print("Ни в одном магазине нет книг Маяковского")
