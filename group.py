from functions import arrangebyGender, arrangebyGPA, assign_to_groups

with open('new_records.csv','r') as f:
    header = f.readline().strip().split(',')
    students = f.readlines()

    record = {}

    for student in students:
        student = student.strip().split(',')  # to change str to a list of strings
        row = {}
        
        for i in range(len(student)):
            row[header[i]] = student[i]
        
        row['CGPA'] = float(row['CGPA'])

        # Arrange the data based on Tutorial Group
        TG = row['Tutorial Group']

        if TG not in record.keys():
            record[TG] = []
        
        record[TG].append(row)

# Example: record = {'G-1': [{student 1}, {student 2},...]
#                   'G-2': [{student 1}, {student 2},...]}

with open('groups.csv','w', newline='') as f:
    f.write('Group,Tutorial Group,Student ID,School,Name,Gender,CPGA')
    f.write('\n')

    for tutorialGroup in record:
            
        groups = assign_to_groups(record[tutorialGroup])
        
        # to write into a file named 'groups.csv'
        grouped_students = {group_num: group for group_num, group in groups.items()}

        for group_num, group in grouped_students.items():
            total = 0
            for student in group:
                total += float(student['CGPA'])
                average = total / 5

                student['CGPA'] = str(student['CGPA'])
                f.write(str(group_num))
                f.write(',')
                f.write(','.join(student.values()))
                f.write('\n')
            
            f.write(str(round(average,2)))
            f.write('\n')


        