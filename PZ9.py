"""Вариант 27
Организовать словарь на 10 англо-русских слов, обеспечивающий "перевод" английского слова на русский."""

words = {
    'hello': 'привет',
    'world': 'мир', 
    'computer': 'компьютер',
    'program': 'программа',
    'language': 'язык',
    'book': 'книга',
    'house': 'дом',
    'water': 'вода', 
    'time': 'время',
    'friend': 'друг'
}

def translate(word):
    """Перевод слова"""
    return words.get(word.lower(), 'Слово не найдено')

def show_all():
    """Показать все слова"""
    print("\nСловарь:")
    for eng, rus in words.items():
        print(f"{eng} - {rus}")

print("Англо-русский словарь")

while True:
    print("\n1 - Все слова\n2 - Перевод\n0 - Выход")
    choice = input("Выбор: ")
    
    if choice == '1':
        show_all()
    elif choice == '2':
        word = input("Слово: ")
        print(f"Перевод: {translate(word)}")
    elif choice == '0':
        break
    else:
        print("Неверный выбор")

