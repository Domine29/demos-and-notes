from classes.person import Person

class Staff(Person):

    def __init__(self, **kwargs)  -> None:
        super().__init__(kwargs['name'], kwargs['age'], kwargs['role'], kwargs['password'])
        self.employee_id = kwargs['employee_id']

    @classmethod
    def create_staff(cls):

        csv_data = cls.read_csv('./data/staff.csv')

        staff = []
        for record in csv_data:
            staff_member = cls(**record)
            staff.append(staff_member)

        return staff