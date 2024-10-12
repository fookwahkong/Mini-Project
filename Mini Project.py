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

def arrangebySchool(records):
    '''
    This function serves the purpose of arranging the unsorted list of students by School

    Parameter:
    Input: Unsorted list of dictionaries
    Output: Lists of dictionaries in a list
    e.g.output = [
    [{student 1, {student 2}, ...],  #from school 1
    [{student 1}, {student 2}, ...], #from school 2
    [...], ...] 
    '''
    schools = {}
    record = []

    for student in records:
        school = student['School']

        if school not in schools.keys():
            schools[school] = []
        
        schools[school].append(student)

    for students in schools.values():
        record.append(students)

    return record



def arrangebyGender(records):
    '''
    This function serves the purpose of arranging the list of students sorted by School 
    '''
    # males = []
    # females = []

    # for student in records:
    #     if student['Gender'] == 'Male':
    #         males.append(student)
    #     else:
    #         females.append(student)

    # return males + females
    record = []

    for students in records:
        group = {'Male': [], 
             'Female': []}

        for student in students:
            if student['Gender'] == 'Male':
                group['Male'].append(student)
            else:
                group['Female'].append(student)

        record.append(group)

    return record


def arrangebyGPA(records):
    new = []
    for row in records:
        # print(row)
        #row = {'Male': [{'Tutorial Group': 'G-1', 'Student ID': '5002', 'School': 'CCDS', 'Name': 'Aarav Singh', 'Gender': 'Male', 'CGPA': 4.02}], 
        # 'Female': [{'Tutorial Group': 'G-1', 'Student ID': '4479', 'School': 'CCDS', 'Name': 'Amelia Kim', 'Gender': 'Female', 'CGPA': 4.11},
        # {'Tutorial Group': 'G-1', 'Student ID': '4402', 'School': 'CCDS', 'Name': 'Grace Turner', 'Gender': 'Female', 'CGPA': 4.08}]}
        for students in row.values():  
            #students = [students in dictionary]
            record = sorted(students, key=lambda d: d['CGPA'])
            new += record 
    return new


#test

a = arrangebySchool(records)
b = arrangebyGender(a)
c = arrangebyGPA(b)
for line in c:
    print(line)
# for line in a:
#     b = arrangebyGender(line)
#     new.append(b)

# for line in new:
#     print(line)

# print(arrangebyGender)
# print(b)
# for row in a:
#     print(row)
# for row in b:
#     for a in row.values():
#         print(a)
# print(b)
# for row in c:
#     for a in row.values():
#         print(a)
# for line in c:    
#     print(line)

import csv
with open('new_records.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Tutorial Group', 'Student ID', 'School', 'Name', 'Gender', 'CPGA'])
    for line in c:
        writer.writerow(line.values())
    
