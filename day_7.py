class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'NAME: {self.full_name}, AGE: {self.age}, MARRITAL STATUS: {self.is_married}')



class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks
        for subject, mark in self.marks.items():

            print(f'{subject}: {mark}')

        print(f'Average mark: {self.average_mark():.2f}')

    def __str__(self):
        return f'STUDET NAME: {self.full_name}, AGE: {self.age}, OBJECTS: {self.marks}'

    def average_mark(self):
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        return total / len(self.marks)




class Teacher(Person):
    basic_salary = 500

    def __init__(self, full_name, age, is_married=None, experience=0):
        super().__init__(full_name, age, is_married)
        self.experience = experience


    def salary_counter(self):
        salary = self.basic_salary
        total_salary = salary
        if self.experience > 3:
            extra_year = self.experience - 3
            bonus = salary * 0.05
            total_salary = salary + extra_year * bonus
        return total_salary


def create_students():
    students_list = []
    student1 = Student('Anatoliy', 24, False,  {
        'math': 5,
        'history': 4,
        'camistry': 3,
        'biology': 4,
        'english': 5
    })
    student2 = Student('Tamara', 26, False,  {
        'math': 4,
        'history': 5,
        'camistry': 4,
        'biology': 5,
        'english': 3
    })
    student3 = Student('Vasiliy', 22, False,  {
        'math': 5,
        'history': 4,
        'camistry': 4,
        'biology': 5,
        'english': 2
    })
    students_list.append(student1)
    students_list.append(student2)
    students_list.append(student3)
    return students_list


students = create_students()


for student in students:
    print(student)


teachers = Teacher('Mariya', 23, 'married', 6)
print(f'NAME: {teachers.full_name} \nAGE: {teachers.age} \n'
      f'MARRITAL STATUS: {teachers.is_married}'
      f'\nEXPERIENCE: {teachers.experience} \nSALARY: {teachers.salary_counter()} ')