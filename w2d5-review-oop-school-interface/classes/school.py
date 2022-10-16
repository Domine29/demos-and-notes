from classes.student import Student
from classes.staff import Staff


class School:
    def __init__(self, name):
        self.name = name
        self.staff = self.initialize_staff()
        self.students = self.initialize_students()

    def initialize_students(self):
        return Student.create_students()

    def initialize_staff(self):
        return Staff.create_staff()

    def list_students(self):
        return self.students

    def get_student(self, id):
        filtered = list(filter( lambda x: x.school_id == id , self.students))
        if len(filtered) == 0 :
            return 'Please input a valid ID'

        return filtered[0]

    def add_student(self, student):
        new_student = Student(**student)
        self.students.append(new_student)

        return new_student

    def delete_student(self, id):
        filtered = list(filter( lambda x: x.school_id == id , self.students))
        if len(filtered) == 0 :
            return 'Student not found'
        else:
            self.students.remove(filtered[0])
            return f'Student {filtered[0].school_id} deleted'
    

