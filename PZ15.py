'''**Вариант 27**

Приложение **_ИНТЕРНЕТ-МАГАЗИН_** для некоторой организации. БД должна

содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
единицу измерения (штуки, килограммы, литры), количество, стоимость.'''

import sqlite3
from datetime import datetime

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT NOT NULL,
            product TEXT NOT NULL,
            unit TEXT NOT NULL,
            quantity REAL NOT NULL,
            price REAL NOT NULL,
            total REAL NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Добавление записи о продаже
def add_sale(customer, product, unit, quantity, price):
    total = quantity * price
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO sales (customer, product, unit, quantity, price, total, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (customer, product, unit, quantity, price, total, date))
    
    conn.commit()
    conn.close()
    print(f"Продажа добавлена. Общая стоимость: {total} руб.")

# Просмотр всех продаж
def view_sales():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    
    print("\n" + "="*80)
    print("ТАБЛИЦА ПРОДАЖ")
    print("="*80)
    print(f"{'ID':<3} {'Покупатель':<15} {'Товар':<15} {'Ед.изм':<10} {'Кол-во':<8} {'Цена':<8} {'Сумма':<10} {'Дата':<10}")
    print("-"*80)
    
    total_revenue = 0
    for sale in sales:
        print(f"{sale[0]:<3} {sale[1]:<15} {sale[2]:<15} {sale[3]:<10} {sale[4]:<8} {sale[5]:<8} {sale[6]:<10} {sale[7]:<10}")
        total_revenue += sale[6]
    
    print("-"*80)
    print(f"ОБЩАЯ ВЫРУЧКА: {total_revenue} руб.")
    conn.close()

# Поиск продаж по покупателю
def find_sales_by_customer(customer):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sales WHERE customer = ?', (customer,))
    sales = cursor.fetchall()
    
    print(f"\nПродажи для покупателя '{customer}':")
    print("-"*60)
    total = 0
    for sale in sales:
        print(f"{sale[2]} - {sale[4]} {sale[3]} - {sale[6]} руб.")
        total += sale[6]
    
    print(f"Итого: {total} руб.")
    conn.close()

# Основная программа
def main():
    create_database()
    
    # Добавление тестовых данных
    test_data = [
        ("Иванов И.И.", "Хлеб", "шт", 2, 50),
        ("Петров П.П.", "Молоко", "л", 1.5, 80),
        ("Сидоров С.С.", "Яблоки", "кг", 2, 120),
        ("Иванов И.И.", "Сахар", "кг", 1, 60),
        ("Козлова А.В.", "Масло", "шт", 1, 150)
    ]
    
    for data in test_data:
        add_sale(*data)
    
    while True:
        print("\n" + "="*40)
        print("ИНТЕРНЕТ-МАГАЗИН")
        print("="*40)
        print("1 - Просмотреть все продажи")
        print("2 - Добавить новую продажу")
        print("3 - Найти продажи по покупателю")
        print("4 - Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            view_sales()
        elif choice == '2':
            customer = input("Покупатель: ")
            product = input("Товар: ")
            unit = input("Единица измерения (шт/кг/л): ")
            quantity = float(input("Количество: "))
            price = float(input("Цена за единицу: "))
            add_sale(customer, product, unit, quantity, price)
        elif choice == '3':
            customer = input("Введите имя покупателя: ")
            find_sales_by_customer(customer)
        elif choice == '4':
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
