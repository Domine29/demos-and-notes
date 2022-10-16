from classes.school import School



cp = School('Code Platoon')
# print(vars(cp))

# for student in cp.students:
#     print(student.name)


selection = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

while(selection != '5'):
    
    match selection:
        case '1':
            student_list = cp.list_students()
            for student in student_list:
                print(student)
            
        case '2':
            id = input("\nPlease input a student id number \n")        #13345
            student_record = cp.get_student(id)
            print(student_record)

        case '3': 
            new_student = { 'role' : 'Student'}
            new_student['name'] = input('Student name: ')
            new_student['school_id'] = input('Student id: ')
            new_student['age'] = input('Student age: ')
            new_student['password'] = input('Student password: ')
            print(cp.add_student(new_student))
        case '4':
            id = input("\nPlease input a student id number \n")        #13345
            print(cp.delete_student(id))

        case _:
            print("Please enter a valid option")

    selection = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")


print ('you are exiting the program')





