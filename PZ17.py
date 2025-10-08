'''
 Вариант 27
 Задание 1. В соответствии с номером варианта перейти по ссылку на прототип.
 Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу
 (см. таблицу 1).
 Задание 2. Разработать программу с применением пакета tk,
 взяв в качестве условия одну любую задачу из ПЗ №№ 2 – 9.
 Задание 3.
 Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
 оформленный согласно требованиям. Все задания выполняются с использованием модуля OS:
 Все задания были объеденены в один код и представлены ниже'''


import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import shutil
import subprocess
from pathlib import Path

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Комплексная программа: 3 задания")
        self.root.geometry("800x600")
        
        # Создаем панель вкладок
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Создаем вкладки для каждого задания
        self.create_tab1()  # Задание 1 - Прототип
        self.create_tab2()  # Задание 2 - Калькулятор
        self.create_tab3()  # Задание 3 - Работа с файлами
        
    def create_tab1(self):
        """Задание 1 - Прототип интерфейса"""
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Задание 1 - Прототип")
        
        # Заголовок
        title_label = ttk.Label(tab1, text="Форма регистрации студента", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(20, 10))
        
        # Основной фрейм для полей ввода
        form_frame = ttk.Frame(tab1)
        form_frame.pack(pady=20, padx=50, fill='x')
        
        # Поле Имя
        ttk.Label(form_frame, text="Имя:").grid(row=0, column=0, sticky='w', pady=5)
        self.name_entry = ttk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, sticky='ew', pady=5, padx=(10, 0))
        
        # Поле Фамилия
        ttk.Label(form_frame, text="Фамилия:").grid(row=1, column=0, sticky='w', pady=5)
        self.surname_entry = ttk.Entry(form_frame, width=30)
        self.surname_entry.grid(row=1, column=1, sticky='ew', pady=5, padx=(10, 0))
        
        # Поле Оценки
        ttk.Label(form_frame, text="Оценки (через запятую):").grid(row=2, column=0, sticky='w', pady=5)
        self.grades_entry = ttk.Entry(form_frame, width=30)
        self.grades_entry.grid(row=2, column=1, sticky='ew', pady=5, padx=(10, 0))
        self.grades_entry.insert(0, "5,4,3,5,4")
        
        # Фрейм для кнопок
        button_frame = ttk.Frame(tab1)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Рассчитать средний балл", 
                  command=self.calculate_average).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Очистить", 
                  command=self.clear_form).pack(side='left', padx=5)
        
        # Поле для вывода результата
        self.result_label = ttk.Label(tab1, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
        # Настройка расширения
        form_frame.columnconfigure(1, weight=1)
    
    def create_tab2(self):
        """Задание 2 - Калькулятор"""
        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab2, text="Задание 2 - Калькулятор")
        
        # Переменная для результата
        self.calc_var = tk.StringVar(value="0")
        
        # Поле ввода калькулятора
        calc_entry = ttk.Entry(tab2, textvariable=self.calc_var, font=("Arial", 14), 
                              justify="right", state="readonly")
        calc_entry.pack(fill='x', padx=20, pady=20)
        
        # Фрейм для кнопок калькулятора
        button_frame = ttk.Frame(tab2)
        button_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Кнопки калькулятора
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '⌫',
            '1', '2', '3', '-', '(',
            '0', '.', '=', '+', ')'
        ]
        
        row, col = 0, 0
        for button in buttons:
            if button == '=':
                cmd = self.calculate
            elif button == 'C':
                cmd = self.clear_calculator
            elif button == '⌫':
                cmd = self.backspace
            else:
                cmd = lambda b=button: self.button_click(b)
            
            ttk.Button(button_frame, text=button, command=cmd,
                      width=6).grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            
            col += 1
            if col > 4:
                col = 0
                row += 1
        
        # Настройка расширения кнопок
        for i in range(5):
            button_frame.columnconfigure(i, weight=1)
        for i in range(4):
            button_frame.rowconfigure(i, weight=1)
    
    def create_tab3(self):
        """Задание 3 - Работа с файлами"""
        tab3 = ttk.Frame(self.notebook)
        self.notebook.add(tab3, text="Задание 3 - Файлы")
        
        # Текстовое поле для вывода
        self.output_text = scrolledtext.ScrolledText(tab3, width=80, height=20, font=("Consolas", 10))
        self.output_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Фрейм для кнопок
        button_frame = ttk.Frame(tab3)
        button_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(button_frame, text="1. Список файлов PZ11", 
                  command=self.list_pz11_files).pack(side='left', padx=2)
        ttk.Button(button_frame, text="2. Создать папки test", 
                  command=self.create_test_folders).pack(side='left', padx=2)
        ttk.Button(button_frame, text="3. Найти короткое имя", 
                  command=self.find_shortest_name).pack(side='left', padx=2)
        ttk.Button(button_frame, text="4. Запустить PDF", 
                  command=self.open_pdf).pack(side='left', padx=2)
        ttk.Button(button_frame, text="5. Удалить test.txt", 
                  command=self.delete_test_file).pack(side='left', padx=2)
        ttk.Button(button_frame, text="Очистить вывод", 
                  command=self.clear_output).pack(side='left', padx=2)
    
    # Методы для Задания 1
    def calculate_average(self):
        """Рассчет среднего балла студента"""
        try:
            name = self.name_entry.get()
            surname = self.surname_entry.get()
            grades_str = self.grades_entry.get()
            
            if not name or not surname or not grades_str:
                messagebox.showwarning("Предупреждение", "Заполните все поля!")
                return
            
            # Преобразуем оценки в числа
            grades = [float(grade.strip()) for grade in grades_str.split(',')]
            average = sum(grades) / len(grades)
            
            # Определяем статус
            status = "отличник" if average >= 4.5 else "хорошист" if average >= 3.5 else "троечник"
            
            result = (f"Студент: {name} {surname}\n"
                     f"Средний балл: {average:.2f}\n"
                     f"Статус: {status}")
            
            self.result_label.config(text=result)
            
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный формат оценок! Используйте числа через запятую.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def clear_form(self):
        """Очистка формы"""
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.grades_entry.delete(0, tk.END)
        self.grades_entry.insert(0, "5,4,3,5,4")
        self.result_label.config(text="")
    
    # Методы для Задания 2
    def button_click(self, value):
        """Обработка нажатия кнопок калькулятора"""
        current = self.calc_var.get()
        if current == "0":
            self.calc_var.set(value)
        else:
            self.calc_var.set(current + value)
    
    def calculate(self):
        """Вычисление выражения"""
        try:
            result = eval(self.calc_var.get())
            self.calc_var.set(str(result))
        except:
            messagebox.showerror("Ошибка", "Некорректное математическое выражение")
    
    def clear_calculator(self):
        """Очистка калькулятора"""
        self.calc_var.set("0")
    
    def backspace(self):
        """Удаление последнего символа"""
        current = self.calc_var.get()
        if len(current) > 1:
            self.calc_var.set(current[:-1])
        else:
            self.calc_var.set("0")
    
    # Методы для Задания 3
    def log_output(self, message):
        """Вывод сообщения в текстовое поле"""
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)
        self.root.update()
    
    def list_pz11_files(self):
        """1. Список файлов в PZ11"""
        self.log_output("\n=== 1. Файлы в каталоге PZ11 ===")
        try:
            pz11_path = Path("PZ11")
            if pz11_path.exists():
                files = [f for f in pz11_path.iterdir() if f.is_file()]
                if files:
                    for file in files:
                        self.log_output(f"  - {file.name}")
                else:
                    self.log_output("  Файлы не найдены")
            else:
                self.log_output("  Каталог PZ11 не найден")
                self.log_output("  Создайте каталог PZ11 с файлами для тестирования")
        except Exception as e:
            self.log_output(f"  Ошибка: {e}")
    
    def create_test_folders(self):
        """2. Создание папок test и работа с файлами"""
        self.log_output("\n=== 2. Создание папок test ===")
        try:
            # Создаем папки
            test_path = Path("test")
            test1_path = test_path / "test1"
            
            test1_path.mkdir(parents=True, exist_ok=True)
            self.log_output("  Папки test/test1 созданы")
            
            # Создаем тестовые файлы если их нет
            self.create_sample_files()
            
            # Копируем файлы (имитация из PZ6 и PZ7)
            pz6_files = list(Path("PZ6").glob("*"))[:2] if Path("PZ6").exists() else []
            pz7_files = list(Path("PZ7").glob("*"))[:1] if Path("PZ7").exists() else []
            
            for i, file in enumerate(pz6_files[:2]):
                shutil.copy2(file, test_path / f"file_from_pz6_{i+1}{file.suffix}")
                self.log_output(f"  Создан файл: test/file_from_pz6_{i+1}{file.suffix}")
            
            for file in pz7_files[:1]:
                new_file = test1_path / "test.txt"
                shutil.copy2(file, new_file)
                self.log_output(f"  Создан файл: test/test1/test.txt")
            
            # Выводим информацию о размерах
            total_size = 0
            for item in test_path.iterdir():
                if item.is_file():
                    size = item.stat().st_size
                    total_size += size
                    self.log_output(f"  Файл: {item.name}, Размер: {size} байт")
            
            self.log_output(f"  Общий размер файлов: {total_size} байт")
            
        except Exception as e:
            self.log_output(f"  Ошибка: {e}")
    
    def find_shortest_name(self):
        """3. Поиск файла с самым коротким именем"""
        self.log_output("\n=== 3. Файл с самым коротким именем в PZ11 ===")
        try:
            pz11_path = Path("PZ11")
            if pz11_path.exists():
                files = [f for f in pz11_path.iterdir() if f.is_file()]
                if files:
                    shortest_file = min(files, key=lambda x: len(x.stem))
                    self.log_output(f"  Самый короткий файл: {shortest_file.name}")
                else:
                    self.log_output("  Файлы не найдены")
            else:
                self.log_output("  Каталог PZ11 не найден")
        except Exception as e:
            self.log_output(f"  Ошибка: {e}")
    
    def open_pdf(self):
        """4. Запуск PDF файла"""
        self.log_output("\n=== 4. Поиск и запуск PDF файла ===")
        try:
            pdf_files = list(Path(".").rglob("*.pdf"))
            if pdf_files:
                pdf_file = pdf_files[0]
                self.log_output(f"  Найден PDF: {pdf_file}")
                self.log_output(f"  Запуск файла...")
                os.startfile(str(pdf_file))
            else:
                self.log_output("  PDF файлы не найдены")
                # Создаем демо-файл для тестирования
                demo_pdf = Path("demo_document.pdf")
                with open(demo_pdf, 'w') as f:
                    f.write("This is a demo PDF file for testing")
                self.log_output("  Создан демо-файл: demo_document.pdf")
                
        except Exception as e:
            self.log_output(f"  Ошибка: {e}")
    
    def delete_test_file(self):
        """5. Удаление файла test.txt"""
        self.log_output("\n=== 5. Удаление файла test.txt ===")
        try:
            test_file = Path("test/test1/test.txt")
            if test_file.exists():
                test_file.unlink()
                self.log_output("  Файл test.txt удален")
            else:
                self.log_output("  Файл test.txt не найден")
        except Exception as e:
            self.log_output(f"  Ошибка: {e}")
    
    def create_sample_files(self):
        """Создание тестовых файлов и папок для демонстрации"""
        # Создаем папки PZ6, PZ7, PZ11 если их нет
        for folder in ["PZ6", "PZ7", "PZ11"]:
            Path(folder).mkdir(exist_ok=True)
        
        # Создаем несколько тестовых файлов
        sample_files = {
            "PZ6": ["main.py", "utils.py", "data.csv"],
            "PZ7": ["report.txt", "analysis.py"],
            "PZ11": ["a.txt", "program.py", "data_file.csv", "readme.md"]
        }
        
        for folder, files in sample_files.items():
            for file in files:
                file_path = Path(folder) / file
                if not file_path.exists():
                    with open(file_path, 'w') as f:
                        f.write(f"# Sample file {file}\nprint('Hello from {file}')")
    
    def clear_output(self):
        """Очистка текстового вывода"""
        self.output_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


