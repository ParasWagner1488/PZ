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
    
    if not sales:
        print(f"Продажи для покупателя '{customer}' не найдены.")
        return
    
    print(f"\nПродажи для покупателя '{customer}':")
    print("-"*60)
    total = 0
    for sale in sales:
        print(f"ID: {sale[0]} - {sale[2]} - {sale[4]} {sale[3]} - {sale[6]} руб.")
        total += sale[6]
    
    print(f"Итого: {total} руб.")
    conn.close()

# Удаление продажи по ID
def delete_sale(sale_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    # Проверяем существование записи
    cursor.execute('SELECT * FROM sales WHERE id = ?', (sale_id,))
    sale = cursor.fetchone()
    
    if sale:
        cursor.execute('DELETE FROM sales WHERE id = ?', (sale_id,))
        conn.commit()
        print(f"Продажа с ID {sale_id} успешно удалена.")
    else:
        print(f"Продажа с ID {sale_id} не найдена.")
    
    conn.close()

# Обновление информации о продаже
def update_sale(sale_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    # Проверяем существование записи
    cursor.execute('SELECT * FROM sales WHERE id = ?', (sale_id,))
    sale = cursor.fetchone()
    
    if not sale:
        print(f"Продажа с ID {sale_id} не найдена.")
        conn.close()
        return
    
    print(f"\nТекущие данные продажи ID {sale_id}:")
    print(f"Покупатель: {sale[1]}")
    print(f"Товар: {sale[2]}")
    print(f"Единица измерения: {sale[3]}")
    print(f"Количество: {sale[4]}")
    print(f"Цена: {sale[5]} руб.")
    print(f"Сумма: {sale[6]} руб.")
    
    print("\nВведите новые данные (оставьте пустым для сохранения текущего значения):")
    
    customer = input(f"Покупатель [{sale[1]}]: ") or sale[1]
    product = input(f"Товар [{sale[2]}]: ") or sale[2]
    unit = input(f"Единица измерения [{sale[3]}]: ") or sale[3]
    
    quantity_input = input(f"Количество [{sale[4]}]: ")
    quantity = float(quantity_input) if quantity_input else sale[4]
    
    price_input = input(f"Цена за единицу [{sale[5]}]: ")
    price = float(price_input) if price_input else sale[5]
    
    total = quantity * price
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        UPDATE sales 
        SET customer = ?, product = ?, unit = ?, quantity = ?, price = ?, total = ?, date = ?
        WHERE id = ?
    ''', (customer, product, unit, quantity, price, total, date, sale_id))
    
    conn.commit()
    conn.close()
    print(f"Продажа с ID {sale_id} успешно обновлена.")
    print(f"Новая общая стоимость: {total} руб.")

# Поиск продажи по ID для просмотра деталей
def find_sale_by_id(sale_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sales WHERE id = ?', (sale_id,))
    sale = cursor.fetchone()
    
    if sale:
        print(f"\nДетали продажи ID {sale_id}:")
        print("-"*40)
        print(f"Покупатель: {sale[1]}")
        print(f"Товар: {sale[2]}")
        print(f"Единица измерения: {sale[3]}")
        print(f"Количество: {sale[4]}")
        print(f"Цена за единицу: {sale[5]} руб.")
        print(f"Общая стоимость: {sale[6]} руб.")
        print(f"Дата продажи: {sale[7]}")
    else:
        print(f"Продажа с ID {sale_id} не найдена.")
    
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
        print("4 - Найти продажу по ID")
        print("5 - Обновить продажу")
        print("6 - Удалить продажу")
        print("7 - Выход")
        
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
            try:
                sale_id = int(input("Введите ID продажи: "))
                find_sale_by_id(sale_id)
            except ValueError:
                print("Ошибка: Введите корректный ID (число).")
        elif choice == '5':
            try:
                sale_id = int(input("Введите ID продажи для обновления: "))
                update_sale(sale_id)
            except ValueError:
                print("Ошибка: Введите корректный ID (число).")
        elif choice == '6':
            try:
                sale_id = int(input("Введите ID продажи для удаления: "))
                # Показываем детали перед удалением
                find_sale_by_id(sale_id)
                confirm = input("Вы уверены, что хотите удалить эту продажу? (y/n): ")
                if confirm.lower() == 'y':
                    delete_sale(sale_id)
                else:
                    print("Удаление отменено.")
            except ValueError:
                print("Ошибка: Введите корректный ID (число).")
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()