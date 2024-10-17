from functions import arrangebyGender, arrangebyGPA, arrangebySchool

'''
Arrange the "records" file such that the data is stored in dictionaries in a list
Within each dictionary, the header (first line in the file) is used for the key and the values are matched accordingly

Example:

[{'Tutorial Group': 'G-1', 'Student ID': '5002', 'School': 'CCDS', 'Name': 'Aarav Singh', 'Gender': 'Male', 'CGPA': '4.02'},
{'Tutorial Group': 'G-1', 'Student ID': '3838', 'School': 'EEE', 'Name': 'Aarti Nair', 'Gender': 'Female', 'CGPA': '4.05'},
...,
{'Tutorial Group': 'G-99', 'Student ID': '1554', 'School': 'SSS', 'Name': 'Zion Tan', 'Gender': 'Male', 'CGPA': '4'}]

'''
with open('records.csv','r') as f:
    header = f.readline().strip().split(',')
    file = f.readlines()

    records = []

    for student in file:
        student = student.strip().split(',')  # to change str to a list of strings
        record = {}
        
        for i in range(len(student)):
            record[header[i]] = student[i]

        record['CGPA'] = float(record['CGPA'])
        records.append(record)

#arrange the data based on tutorial group
new_records = {}
for student in records:
    tutorialGroup = student['Tutorial Group']
    if tutorialGroup not in new_records.keys():
        new_records[tutorialGroup] = []
    
    new_records[tutorialGroup].append(student)


with open('new_records.csv','w', newline='') as f:
    
    f.write('Tutorial Group,Student ID,School,Name,Gender,CGPA\n')

    #within the tutorial group, arrange the data based on the student's school
    for tutorialGroup in new_records:
        studentsinSchool = arrangebySchool(new_records[tutorialGroup])

        #within tutorial and school, arrange the data based on gender
        for school in studentsinSchool:
            studentsinSchoolGender = arrangebyGender(studentsinSchool[school])

            #within tutorial, school and gender, arrange the data based on GPA
            for gender in studentsinSchoolGender:
                studentsinSchoolGenderGPA = arrangebyGPA(studentsinSchoolGender[gender])
                for student in studentsinSchoolGenderGPA:
                    student['CGPA'] = str(student['CGPA'])
                    f.write(','.join(student.values()))
                    f.write('\n')

 




    
