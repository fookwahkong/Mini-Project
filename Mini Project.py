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
    'School 1': [{student 1, {student 2}, ...],  
    'School 2': [{student 1}, {student 2}, ...], 
    'School 3': [...], ...] 
    '''
    schools = {}
    record = []

    for student in records:
        school = student['School']

        if school not in schools.keys():
            schools[school] = []
        
        schools[school].append(student)

    return schools

def arrangebyGender(records):
    '''
    This function serves the purpose of arranging the list of students sorted by School 
    '''
    males = []
    females = []

    for student in records:
        if student['Gender'] == 'Male':
            males.append(student)
        else:
            females.append(student)
    
    record = {'Male': males,
              'Female': females}
    
    return record 

def arrangebyGPA(records):
    
    records.sort(key=lambda d: -d['CGPA'])
    print(records)
    return records

#test
record_bySchoolGenderGPA = {}
record = records[:20]
record_bySchool = arrangebySchool(record)

for item in record_bySchool.values():
    school = item[0]['School']

    record_byGender = arrangebyGender(item)
    gender = record_byGender.keys()

    record_byGenderGPA = {}
    for gender in record_byGender.keys():
 
        record_byGenderGPA[gender] = arrangebyGPA(record_byGender[gender])
        

    if school not in record_bySchoolGenderGPA.keys():   
        record_bySchoolGenderGPA[school] = record_byGenderGPA

# num_groups = 120
# groups = [[] for _ in range(num_groups)]

# # Step 4: Manually assign students to groups by alternating between subgroups
# group_index = 0

# for school in final:
#     for gender in final[school]:
#         for student in final[school][gender]:
#             groups[group_index].append(student)
#             group_index = (group_index + 1) % num_groups  # Rotate between groups

# import csv
# with open('new_records.csv','w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Tutorial Group', 'Student ID', 'School', 'Name', 'Gender', 'CPGA'])
#     for line in c:
#         writer.writerow(line.values())
    
