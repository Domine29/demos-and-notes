import csv
# -------------------------------
# import pandas as pd
  
# # Read a csv file to a dataframe using mutiple delimiters
# student_csv =  pd.read_csv('students.csv', sep='[:,;|_]', engine='python')
# print(student_csv)

# -------------------------------

# file = open('./example.csv', 'w')
# file.write('hello, world')
# file.close()

# -------------------------------
people = []
with open('./example.csv', 'r') as csvfile:

    # csvreader = csv.reader(csvfile, delimiter=',')
    # next(csvreader)

    # for row in csvreader:
    #     print(type(row))
    #     print(row[0])
    #     # print(' '.join(row))

    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        print(type(row))

        print(row['name'])
        
        people.append(row)

        print(' '.join(row))
print(people)