from classes.person import Person

class Student(Person):

    def __init__(self, **kwargs)  -> None:
        super().__init__(kwargs['name'], kwargs['age'], kwargs['role'], kwargs['password'])
        self.school_id = kwargs['school_id']

    @classmethod
    def create_students(cls):

        csv_data = cls.read_csv('./data/students.csv')

        students = []
        for record in csv_data:
            student = cls(**record)
            students.append(student)

        return students

    def add_student_to_csv(self, **kwargs):
        
        pass



    def __str__(self):
        return f'name: {self.name}, id: {self.school_id}, role: {self.role}'




        
