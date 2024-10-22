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
with open('groups2.csv','w', newline='') as f:
    f.write('Group,Tutorial Group,Student ID,School,Name,Gender,CPGA')
    f.write('\n')
    for tutorialGroup in record:

        all_students = [student for student in record[tutorialGroup]]
            
        all_students.sort(key=lambda x:x['CGPA'], reverse=True)

        total_number = len(all_students)

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
        
        group_gender = {0: {"Male_count": 0, "Female_count": 0},
                        1: {"Male_count": 0, "Female_count": 0},
                        2: {"Male_count": 0, "Female_count": 0},
                        3: {"Male_count": 0, "Female_count": 0},
                        4: {"Male_count": 0, "Female_count": 0},
                        5: {"Male_count": 0, "Female_count": 0},
                        6: {"Male_count": 0, "Female_count": 0},
                        7: {"Male_count": 0, "Female_count": 0},
                        8: {"Male_count": 0, "Female_count": 0},
                        9: {"Male_count": 0, "Female_count": 0}}

        total_number = len(all_students)
        no_students = 0
        duplicate_schools = 0
        while (no_students == 0) and (duplicate_schools == 0):
            not_appended = 0 #Count how many times in the for-loop which resulted in nothing happening
            for group_index in range(len(groups)):
                total_students_before = len(all_students) #Amount of students before appending  process for each group
                if len(groups[group_index]) != (total_number/len(groups)):
                    for index,students in enumerate(all_students):
                            if (group_gender[group_index]["Male_count"] < float(((total_number/len(groups))/2))) and (group_gender[group_index]["Female_count"] < float(((total_number/len(groups))/2))):
                                if students['School'] not in [group_student['School'] for group_student in groups[group_index]]: #Check for repeated Schools
                                    if students['Gender'] == 'Male':
                                        group_gender[group_index]["Male_count"] += 1
                                    else:
                                        group_gender[group_index]["Female_count"] += 1

                                    groups[group_index].append(all_students.pop(index)) #Appends and pops a male of the highest GPA of the total_students dictionary (top of dict)
                                    break
                                else:
                                    continue
                            if (group_gender[group_index]["Male_count"] > float(((total_number/len(groups))/2))):
                                if (students['School'] not in [group_student['School'] for group_student in groups[group_index]]) and (students['Gender'] == 'Female'):
                                    groups[group_index].append(all_students.pop(index))
                                    group_gender[group_index]["Female_count"] += 1
                                    break
                                else:
                                    continue
                            if (group_gender[group_index]["Female_count"] > float(((total_number/len(groups))/2))):
                                if (students['School'] not in [group_student['School'] for group_student in groups[group_index]]) and (students['Gender'] == 'Male'):
                                    groups[group_index].append(all_students.pop(index))
                                    group_gender[group_index]["Male_count"] += 1
                                    break
                                else:
                                    continue

                    for index,students in enumerate(reversed(all_students)):
                            if (group_gender[group_index]["Male_count"] < float(((total_number/len(groups))/2))) and (group_gender[group_index]["Female_count"] < float(((total_number/len(groups))/2))):
                                if students['School'] not in [group_student['School'] for group_student in groups[group_index]]: #Check for repeated Schools
                                    if students['Gender'] == 'Male':
                                        group_gender[group_index]["Male_count"] += 1
                                    else:
                                        group_gender[group_index]["Female_count"] += 1

                                    groups[group_index].append(all_students.pop(index)) #Appends and pops a male of the highest GPA of the total_students dictionary (top of dict)
                                    break
                                else:
                                    continue
                            if (group_gender[group_index]["Male_count"] > float(((total_number/len(groups))/2))):
                                if (students['School'] not in [group_student['School'] for group_student in groups[group_index]]) and (students['Gender'] == 'Female'):
                                    groups[group_index].append(all_students.pop(index))
                                    break
                                else:
                                    continue
                            if (group_gender[group_index]["Female_count"] > float(((total_number/len(groups))/2))):
                                if (students['School'] not in [group_student['School'] for group_student in groups[group_index]]) and (students['Gender'] == 'Male'):
                                    groups[group_index].append(all_students.pop(index))
                                    break
                                else:
                                    continue
                            
                total_students_after = len(all_students)
                if total_students_after == total_students_before:
                    not_appended += 1 #Shows how many times out of maximum of 10 times which the for loop skipped everyone (because all that is left are repeated schools)

            if len(all_students) == 0: #If run out of students to append
                no_students += 1

            if not_appended == len(groups): #If went through a full loop of 10 groups where nothing is appended but have leftover students (means duplicate schools for each group which are not filled)
                duplicate_schools += 1
        
        while all_students:
            a
            for group_index in range(len(groups)): #Appends the rest of the students with duplicate schools into the rest of the groups which are not filled
                    if len(groups[group_index]) != (total_number/len(groups)):
                        groups[group_index].append(all_students.pop(0))
                        


        grouped_students = {group_num: group for group_num, group in groups.items()}
        # prnt(grouped_students)

        for group_num, group in grouped_students.items():
            for student in group:
                student['CGPA'] = str(student['CGPA'])
                f.write(str(group_num))
                f.write(',')
                f.write(','.join(student.values()))
                f.write('\n')


        