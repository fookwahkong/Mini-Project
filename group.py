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
        total_students = male_students + female_students # Creates a dictionary of highest male GPA to lowest male GPA and then highest female GPA to lowest female GPA
        total_number = len(total_students)
        no_students = 0
        duplicate_schools = 0

        while (no_students == 0) and (duplicate_schools == 0):
            not_appended = 0 #Count how many times in the for-loop which resulted in nothing happening
            for group_index in range(len(groups)):
                total_students_before = len(total_students) #Amount of students before appending  process for each group
                if len(groups[group_index]) != (total_number/len(groups)):
                    for index,students in enumerate(total_students):
                        if students['School'] not in [group_student['School'] for group_student in groups[group_index]]: #Check for repeated Schools
                            groups[group_index].append(total_students.pop(index)) #Appends and pops a male of the highest GPA of the total_students dictionary (top of dict)
                            break
                        else:
                            continue
                if len(groups[group_index]) != (total_number/len(groups)):
                    for index,students in enumerate(reversed(total_students)):
                        if students['School'] not in [group_student['School'] for group_student in groups[group_index]]:
                            groups[group_index].append(total_students.pop(index)) #Appends and pops a female of the lowest GPA of the total_students dictionary (bottom of dict)
                            break
                        else:
                            continue
            
                total_students_after = len(total_students)
                if total_students_after == total_students_before:
                    not_appended += 1 #Shows how many times out of maximum of 10 times which the for loop skipped everyone (because all that is left are repeated schools)

            if len(total_students) == 0: #If run out of students to append
                no_students += 1

            if not_appended == len(groups): #If went through a full loop of 10 groups where nothing is appended but have leftover students (means duplicate schools for each group which are not filled)
                duplicate_schools += 1
        
        while total_students:
            for group_index in range(len(groups)): #Appends the rest of the students with duplicate schools into the rest of the groups which are not filled
                    if len(groups[group_index]) != (total_number/len(groups)):
                        groups[group_index].append(total_students.pop(0))


        grouped_students = {group_num: group for group_num, group in groups.items()}
        # prnt(grouped_students)

        for group_num, group in grouped_students.items():
            for student in group:
                student['CGPA'] = str(student['CGPA'])
                f.write(str(group_num))
                f.write(',')
                f.write(','.join(student.values()))
                f.write('\n')


        