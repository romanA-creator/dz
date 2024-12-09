class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calculate_average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.calculate_average_grade() < other.calculate_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.calculate_average_grade() < other.calculate_average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка: либо курс не совпадает, либо объект не является студентом."
# Функция для подсчета средней оценки за домашние задания по студентам
def calculate_students_average(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Функция для подсчета средней оценки за лекции лекторов
def calculate_lecturers_average(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Создание объектов классов
student1 = Student('Alice', 'Johnson', 'female')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Math']

student2 = Student('Bob', 'Smith', 'male')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Physics']

reviewer1 = Reviewer('John', 'Reviewer')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Jane', 'Reviewer')
reviewer2.courses_attached += ['Git']

lecturer1 = Lecturer('Dr.', 'Lecturer1')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Dr.', 'Lecturer2')
lecturer2.courses_attached += ['Git']

# Оценки от рецензентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 7)

reviewer2.rate_hw(student2, 'Git', 9)
reviewer2.rate_hw(student2, 'Git', 8)

# Оценки от студентов лекторам
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)

student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Git', 7)

# Вывод информации
print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)

# Сравнение студентов и лекторов
print(f"Student1 has higher average grade than Student2: {student1 > student2}")
print(f"Lecturer1 has higher average grade than Lecturer2: {lecturer1 > lecturer2}")

# Подсчет средней оценки за домашние задания
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

average_student_grade_python = calculate_students_average(students, 'Python')
average_lecturer_grade_python = calculate_lecturers_average(lecturers, 'Python')

print(f"Average grade for Python (students): {average_student_grade_python:.2f}")
print(f"Average grade for Python (lecturers): {average_lecturer_grade_python:.2f}")
