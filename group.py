from functions import arrangebyGender, arrangebyGPA

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
    print('a')
    for tutorialGroup in record:
            
        male_students = arrangebyGender(record[tutorialGroup])['Male']
        female_students = arrangebyGender(record[tutorialGroup])['Female']
        
        male_students = arrangebyGPA(male_students)
        female_students = arrangebyGPA(female_students)
    
        all_students = arrangebyGPA(male_students + female_students)
        
        groups = {0: [],
                  1: [],
                  2: [],
                  3: [],
                  4: [],
                  5: [],
                  6: [],
                  7: [],
                  8: [],
                  9: []}

        team_size = 5


        for i in range(team_size):
            for group_index in range(10):
                student = all_students.pop(0)             # pop the student with highest/lowest GPA

                groups[group_index].append(student)
            
            all_students.reverse()

        #to write into a output file named 'groups.csv'
        grouped_students = {group_num: group for group_num, group in groups.items()}

        for group_num, group in grouped_students.items():
            total = 0
            for student in group:
                total += student['CGPA']
                average = total / 5

                student['CGPA'] = str(student['CGPA'])
                f.write(str(group_num))
                f.write(',')
                f.write(','.join(student.values()))
                f.write('\n')
            
            f.write(str(round(average,2)))
            f.write('\n')


        