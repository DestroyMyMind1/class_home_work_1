class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade in range(1, 11):
            if lecturer in self.courses_in_progress:
                lecturer.lecturer_grade[course] += [grade]
            else:
                lecturer.lecturer_grade[course] = [grade]
        else:
            return ("Ошибка выставления оценки, укажите от 1 до 10!")

    def _middle_grade_student_(self):
        for grade in self.grades.values():
            return sum(grade) / len(grade)

    def __lt__(self,other):
        if not isinstance(other, Student):
            print('Это не студент')
            return
        if (self._middle_grade_student_() > other._middle_grade_student_()) == True:
            return f'Высший средний балл за ДЗ имеет: {self.name} {self.surname}'
        else:
            return f'Высший средний балл за ДЗ имеет: {other.name} {other.surname}'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {round(self._middle_grade_student_(), 1)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

def all_hw(students_list, course):
    sum = 0
    count = 0
    for student in students_list:
         for grade in student.grades[course]:
             sum += grade
             count += 1
    return round(sum / count, 1)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grade = {}

    def _middle_grade_lecturer_(self):
        for grade in self.lecturer_grade.values():
            return sum(grade) / len(grade)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор')
            return
        if (self._middle_grade_lecturer_() > other._middle_grade_lecturer_()) == True:
            return f'Высшую среднюю оценку за лекции имеет: {self.name} {self.surname}'
        else:
            return f'Высшую среднюю оценку за лекции имеет: {other.name} {other.surname}'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self._middle_grade_lecturer_(), 1)}"

def all_lecturers(lecturers_list, course):
    sum = 0
    count = 0
    for lecturer in lecturers_list:
        for grade in lecturer.lecturer_grade[course]:
            sum += grade
            count += 1
    return round(sum / count, 1)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

student_1 = Student('Eden', 'Clapton', 'male')
student_2 = Student('Delia', 'Hailey', 'famale')
mentor_1 = Mentor('Tiller', 'Evans')
mentor_2 = Mentor('Melissa', 'Brickman')
lecturer_1 = Lecturer('Dylan', 'Durham')
lecturer_2 = Lecturer('Set', 'Hill')
reviewer_1 = Reviewer('Mark', 'Haig')
reviewer_2 = Reviewer('Joseph', 'Scott')
student_1.courses_in_progress += ['Git']
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_1.grades['Введение в программирование'] = [9, 9, 9]
student_2.finished_courses += ['Введение в программирование']
student_2.grades['Введение в программирование'] = [9, 10, 10]
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['Python']
reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 7)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 6)
student_1.rate_lecturer(lecturer_1, 'Git', 7)
student_1.rate_lecturer(lecturer_2, 'Git', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 5)
student_2.rate_lecturer(lecturer_2, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Git', 9)
student_2.rate_lecturer(lecturer_2, 'Git', 7)
print(student_1)
print()
print(student_2)
print()
print(student_1.__lt__(student_2))
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(lecturer_1.__lt__(lecturer_2))
print()
print("Средняя оценка за домашние задания по всем студентам в рамках курса Python:")
print(all_hw([student_1, student_2], 'Python'))
print("Средняя оценка за домашние задания по всем студентам в рамках курса Git:")
print(all_hw([student_1, student_2], 'Git'))
print("Средняя оценка за домашние задания по всем студентам в рамках курса Введение в программирование:")
print(all_hw([student_1, student_2], 'Введение в программирование'))
print("Средняя оценка за лекции всех лекторов в рамках курса Python:")
print(all_lecturers([lecturer_1, lecturer_2], 'Python'))
print("Средняя оценка за лекции всех лекторов в рамках курса Git:")
print(all_lecturers([lecturer_1, lecturer_2], 'Git'))
