import csv

with open("../data/students.csv",'r') as student_file:
    reader = csv.DictReader(student_file) #can iterate through
    #students = [list(x) for x in reader]
    for row in reader:
        print(row) #row is each entry of a student