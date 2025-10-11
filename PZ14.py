"""Вариант 27
Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить его в новый текстовый файл."""


def extract_1857_block(input_file, output_file):
    """
    Извлекает блок информации за 1857 год из исходного файла и сохраняет в новый файл
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Ищем начало блока за 1857 год
        start_marker = "1857"
        start_index = content.find(start_marker)
        
        if start_index == -1:
            print("Блок за 1857 год не найден в файле")
            return False
        
        # Ищем конец блока (следующий год или конец файла)
        end_index = -1
        years = ["1858", "1859", "1860", "1861", "1862", "1863", "1864", "1865"]
        
        for year in years:
            end_index = content.find(year, start_index + 1)
            if end_index != -1:
                break
        
        # Если следующий год не найден, берем до конца файла
        if end_index == -1:
            end_index = len(content)
        
        # Извлекаем блок за 1857 год
        block_1857 = content[start_index:end_index].strip()
        
        # Сохраняем в новый файл
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(block_1857)
        
        print(f"Блок за 1857 год успешно извлечен и сохранен в файл: {output_file}")
        print(f"Размер извлеченного блока: {len(block_1857)} символов")
        
        return True
        
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

# Альтернативная версия, если данные структурированы по-другому
def extract_1857_block_alternative(input_file, output_file):
    """
    Альтернативный метод для случаев, когда блоки разделены пустыми строками
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        block_lines = []
        in_1857_block = False
        
        for line in lines:
            # Если находим начало блока 1857 года
            if "1857" in line and not in_1857_block:
                in_1857_block = True
                block_lines.append(line)
            elif in_1857_block:
                # Проверяем, не начался ли следующий блок (следующий год)
                if any(year in line for year in ["1858", "1859", "1860"]):
                    break
                # Или если пустая строка означает конец блока
                elif line.strip() == "" and len(block_lines) > 0:
                    # Можно раскомментировать следующую строку, если пустая строка означает конец блока
                    # break
                    block_lines.append(line)
                else:
                    block_lines.append(line)
        
        if block_lines:
            with open(output_file, 'w', encoding='utf-8') as output:
                output.writelines(block_lines)
            
            print(f"Блок за 1857 год успешно извлечен и сохранен в файл: {output_file}")
            return True
        else:
            print("Блок за 1857 год не найден")
            return False
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

# Основная программа
if __name__ == "__main__":
    input_filename = "Dostoevsky.txt"
    output_filename = "Dostoevsky_1857.txt"
    
    print("Извлечение блока информации за 1857 год...")
    
    # Пробуем первый метод
    success = extract_1857_block(input_filename, output_filename)
    
    # Если первый метод не сработал, пробуем альтернативный
    if not success:
        print("Пробуем альтернативный метод...")
        extract_1857_block_alternative(input_filename, output_filename)
    
    # Показываем preview извлеченного содержимого
    try:
        with open(output_filename, 'r', encoding='utf-8') as file:
            preview = file.read(500)  # Первые 500 символов
            print("\nPreview извлеченного блока:")
            print("=" * 50)
            print(preview)
            if len(preview) == 500:
                print("... (файл продолжается)")
            print("=" * 50)
    except:
        pass