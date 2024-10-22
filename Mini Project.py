from functions import arrangebyGender, arrangebyGPA, arrangebySchool

'''
First, let's start off by importing the data in 'records.csv' into Python

We will do so by storing the data in a list of dictionaries
Within each dictionary, the header (first line in the file) is used for the key and the values are matched accordingly

Example:

[{'Tutorial Group': 'G-1', 'Student ID': '5002', 'School': 'CCDS', 'Name': 'Aarav Singh', 'Gender': 'Male', 'CGPA': '4.02'},
{'Tutorial Group': 'G-1', 'Student ID': '3838', 'School': 'EEE', 'Name': 'Aarti Nair', 'Gender': 'Female', 'CGPA': '4.05'},
...,
{'Tutorial Group': 'G-99', 'Student ID': '1554', 'School': 'SSS', 'Name': 'Zion Tan', 'Gender': 'Male', 'CGPA': '4'}]

'''
with open('records.csv','r') as f:
    header = f.readline().strip().split(',') # extract header of the file and cast it from string to a list of strings 
    file = f.readlines()

    records = []

    for student in file:
        student = student.strip().split(',')  # to cast string to a list of strings
        temp = {}
        
        for i in range(len(student)):
            temp[header[i]] = student[i]

        temp['CGPA'] = float(temp['CGPA'])
        records.append(temp)

# Arrange the data based on tutorial group

new_records = {}
for student in records:
    tutorialGroup = student['Tutorial Group']

    if tutorialGroup not in new_records.keys():
        new_records[tutorialGroup] = []
    
    new_records[tutorialGroup].append(student)

# Example: new_records = {'G-1': [{student 1}, {student 2}, ...], 
#                         'G-2': [{student 1}, ...], 
#                         'G-3': [{student 1}, ...], ...}

#Write the arranged data into new csv file
with open('new_records.csv','w', newline='') as f:
    
    f.write('Tutorial Group,Student ID,School,Name,Gender,CGPA\n')

    # Within the tutorial group, arrange the data based on the student's school
    for tutorialGroup in new_records:
        studentsinSchool = arrangebySchool(new_records[tutorialGroup])

        # Within tutorial and school, arrange the data based on gender
        for school in studentsinSchool:
            studentsinSchoolGender = arrangebyGender(studentsinSchool[school])

            # Within tutorial, school and gender, arrange the data based on GPA
            for gender in studentsinSchoolGender:
                studentsinSchoolGenderGPA = arrangebyGPA(studentsinSchoolGender[gender])
                for student in studentsinSchoolGenderGPA:
                    student['CGPA'] = str(student['CGPA'])
                    f.write(','.join(student.values()))
                    f.write('\n')

 




    
