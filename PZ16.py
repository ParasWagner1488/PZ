'''Создайте класс «Студент», который имеет атрибуты: Имя, Фамилия и Оценки.

Добавьте метод вычисления среднего балла для определения, является ли студент отличником.'''

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def add_grade(self, grade):
        if 2 <= grade <= 5:
            self.grades.append(grade)
        else:
            print("Ошибка: Оценка должна быть от 2 до 5.")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        average = self.calculate_average()
        return average >= 4.5 and all(grade >= 4 for grade in self.grades)

    def __str__(self):
        return f"Студент: {self.name} {self.surname}, Оценки: {self.grades}"


if __name__ == "__main__":
    student1 = Student("Иван", "Иванов")
    
    student1.add_grade(5)
    student1.add_grade(4)
    student1.add_grade(5)
    student1.add_grade(5)
    
    print(student1)
    print(f"Средний балл: {student1.calculate_average():.2f}")
    print(f"Является ли отличником: {'Да' if student1.is_excellent() else 'Нет'}")
