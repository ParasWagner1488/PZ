"""Вариант 27
Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить его в новый текстовый файл."""


"""
ПОСТАНОВКА ЗАДАЧИ:
Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год 
и поместить его в новый текстовый файл.

Требования:
- Использовать регулярные выражения для поиска блоков
- Шаблон должен быть максимально универсальным
- Не вносить изменений в исходный файл
- Код должен соответствовать PEP 8
- Обрабатывать различные форматы данных
"""

import re
import os


def extract_year_block(input_file: str, output_file: str, target_year: int = 1857) -> bool:
    """
    Извлекает блок информации за указанный год из исходного файла 
    и сохраняет в новый файл с использованием регулярных выражений.
    
    Args:
        input_file (str): Путь к исходному файлу
        output_file (str): Путь к выходному файлу
        target_year (int): Год для извлечения (по умолчанию 1857)
    
    Returns:
        bool: True если операция успешна, False в противном случае
    """
    # Проверяем существование исходного файла
    if not os.path.exists(input_file):
        print(f"Ошибка: Файл {input_file} не найден")
        return False
    
    try:
        # Читаем содержимое файла с обработкой различных кодировок
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        try:
            with open(input_file, 'r', encoding='cp1251') as file:
                content = file.read()
        except UnicodeDecodeError:
            print("Ошибка: Не удалось декодировать файл. Проверьте кодировку.")
            return False
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return False
    
    # Универсальное регулярное выражение для поиска блока по году
    # Ищет год в различных форматах: "1857", " 1857 ", "1857:", "1857 год" и т.д.
    year_pattern = rf"""
        ({{0}})                    # Начало блока с годом
        \s*{target_year}\s*       # Искомый год с возможными пробелами
        [^\d]*                    # Любые нецифровые символы после года
        (.*?)                     # Содержимое блока (нежадный поиск)
        (?=\s*\d{{4}}\s*|$)       # Остановка перед следующим годом или концом файла
    """
    
    # Компилируем регулярное выражение с флагами:
    # re.DOTALL - точка включает переносы строк
    # re.VERBOSE - позволяет использовать комментарии и пробелы
    # re.IGNORECASE - игнорирует регистр
    pattern = re.compile(year_pattern.format(r'.*?'), re.DOTALL | re.VERBOSE | re.IGNORECASE)
    
    # Поиск всех совпадений
    matches = pattern.findall(content)
    
    if not matches:
        print(f"Блок за {target_year} год не найден в файле")
        return False
    
    # Извлекаем содержимое блока (вторая группа захвата)
    # Используем списковое включение для фильтрации непустых результатов
    blocks = [match[1].strip() for match in matches if match[1].strip()]
    
    if not blocks:
        print(f"Найден заголовок {target_year} года, но содержимое блока пустое")
        return False
    
    try:
        # Сохраняем все найденные блоки за указанный год
        with open(output_file, 'w', encoding='utf-8') as output:
            for i, block in enumerate(blocks, 1):
                if len(blocks) > 1:
                    output.write(f"=== Блок {i} ===\n")
                output.write(block)
                if len(blocks) > 1 and i < len(blocks):
                    output.write("\n\n" + "="*50 + "\n\n")
        
        print(f"Успешно извлечено {len(blocks)} блок(ов) за {target_year} год")
        print(f"Результат сохранен в файл: {output_file}")
        return True
        
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")
        return False


def preview_extracted_content(output_file: str, max_preview: int = 500) -> None:
    """
    Показывает превью извлеченного содержимого.
    
    Args:
        output_file (str): Путь к файлу для превью
        max_preview (int): Максимальное количество символов для показа
    """
    if not os.path.exists(output_file):
        return
    
    try:
        with open(output_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print(f"\nПревью извлеченного блока ({len(content)} символов):")
        print("=" * 60)
        
        # Генератор для обработки длинного текста
        preview = content[:max_preview]
        print(preview)
        
        if len(content) > max_preview:
            print("... (файл продолжается)")
        print("=" * 60)
            
    except Exception as e:
        print(f"Ошибка при чтении превью: {e}")


def main() -> None:
    """Основная функция программы."""
    # Параметры файлов
    input_filename = "Dostoevsky.txt"
    output_filename = "Dostoevsky_1857.txt"
    target_year = 1857
    
    print("=" * 70)
    print("ПРОГРАММА ДЛЯ ИЗВЛЕЧЕНИЯ БЛОКА ИНФОРМАЦИИ ЗА 1857 ГОД")
    print("=" * 70)
    print(f"Исходный файл: {input_filename}")
    print(f"Выходной файл: {output_filename}")
    print(f"Целевой год: {target_year}")
    print("-" * 70)
    
    # Выполняем извлечение блока
    success = extract_year_block(input_filename, output_filename, target_year)
    
    if success:
        # Показываем превью результата
        preview_extracted_content(output_filename)
    else:
        print("Извлечение блока завершилось неудачно")
    
    print("\nПрограмма завершена.")


# Точка входа в программу
if __name__ == "__main__":
    main()