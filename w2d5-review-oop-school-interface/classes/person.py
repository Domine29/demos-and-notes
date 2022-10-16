import csv

class Person:
    def __init__(self, name, age, role, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role


    def read_csv(file_path):

        l = []
        with open(file_path, 'r' ) as csv_file:
            file_reader = csv.DictReader(csv_file)
            for row in file_reader:
                l.append(row)

            return l

    def __str__():
        print()