from collections import defaultdict

with open('new_records.csv','r') as f:
    header = f.readline().strip().split(',')
    file = f.readlines()

    record = {}
    studentsinTG = []

    for student in file:
        student = student.strip().split(',')  # to change str to a list of strings
        row = {}
        
        for i in range(len(student)):
            row[header[i]] = student[i]
        
        row['CGPA'] = float(row['CGPA'])

        TG = row['Tutorial Group']

        if TG not in record.keys():
            record[TG] = []
        

        record[TG].append(row)

        if row['Tutorial Group'] != TG:
            studentsinTG = []
            
print(record)
with open('groups.csv','w', newline='') as f:

    f.write('Group,Tutorial Group,Student ID,School,Name,Gender,CPGA')
    f.write('\n')
    for tutorialGroup in record:

        male_students = [student for student in record[tutorialGroup] if student['Gender'] == 'Male']
        female_students = [student for student in record[tutorialGroup] if student['Gender'] == 'Female']
            
        male_students.sort(key=lambda x:x['CGPA'], reverse=True)
        female_students.sort(key=lambda x:x['CGPA'], reverse=True)

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

        for group_index in range(10):

            if male_students:
                groups[group_index].append(male_students.pop(0))

            if female_students:
                groups[group_index].append(female_students.pop(0))

        all_students = male_students + female_students
        all_students.sort(key=lambda x:x['CGPA'], reverse=True)

        for i, student in enumerate(all_students):
            groups[i % 10].append(student)

        grouped_students = {group_num: group for group_num, group in groups.items()}
        # prnt(grouped_students)

        

        for group_num, group in grouped_students.items():
            for student in group:
                student['CGPA'] = str(student['CGPA'])
                f.write(str(group_num))
                f.write(',')
                f.write(','.join(student.values()))
                f.write('\n')


print("abc")