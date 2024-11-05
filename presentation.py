import matplotlib.pyplot as plt
import statistics 

with open('groups.csv','r') as f:
    header = f.readline().strip().split(',')

    students = f.readlines()

    groups = {}
    for student in students:
        student = student.strip().split(',')
        
        group_idx = student[0] 
        tutorialGroup = student[1]
        if tutorialGroup not in groups.keys():
            groups[tutorialGroup] = {}

        if group_idx not in groups[tutorialGroup].keys():
            groups[tutorialGroup][group_idx] = []


        groups[tutorialGroup][group_idx].append(student)

#Calculate the average GPA for each group in each tutorialGroup
tutorialGroup_avgGPA = {}

for tutorialGroup in groups:

    groups_GPA = []
    for group_index in groups[tutorialGroup]:
        
        group_totalGPA = 0

        for student in groups[tutorialGroup][group_index]:

            studentGPA = float(student[6])                            #index 6 is where CGPA is at
            group_totalGPA += studentGPA

        group_avgGPA = group_totalGPA / len(groups[tutorialGroup][group_index])

        groups_GPA.append(group_avgGPA) 

    tutorialGroup_avgGPA[tutorialGroup] = groups_GPA

# Using the average GPA of 5 groups in each tutorial group, 
# Calculate the standard deviation of the averageGPA of each tutorialGroup

tutorialGroup_dev = {}
for tutorialGroup in tutorialGroup_avgGPA:
    deviation = statistics.stdev(tutorialGroup_avgGPA[tutorialGroup])

    tutorialGroup_dev[tutorialGroup] = deviation

# Plot graph for GPA
tutorialGroups = list(tutorialGroup_dev.keys())
tutorialGroupDEV = list(tutorialGroup_dev.values())
plt.figure(figsize=(250, 10))
plt.bar(tutorialGroups, tutorialGroupDEV, color='skyblue')

# Adding labels and title
plt.xlabel('Tutorial Group')
plt.ylabel('Standard Deviation')
plt.title('STD of GPA per Tutorial Group')


#plot graph for duplicate schools
groups_with_duplicate_school = {}
for tutorialGroup in groups:
    for group_index in groups[tutorialGroup]:
        duplicate_school = 0

        for student_index in range(len(groups[tutorialGroup][group_index]) - 1):
            student = groups[tutorialGroup][group_index][student_index]
            next_student = groups[tutorialGroup][group_index][student_index + 1]

            #if the group has duplicate school
            if student[3] == next_student[3]:
                duplicate_school += 1


        if duplicate_school != 0:
            groups_with_duplicate_school[f'{tutorialGroup}, Group {group_index}'] = duplicate_school + 1


# plot graph for duplicate schools
group_name = list(groups_with_duplicate_school.keys())
duplicates = list(groups_with_duplicate_school.values())
plt.figure(figsize=(250, 10))
plt.bar(group_name, duplicates, color='skyblue')

# Adding labels and title
plt.xlabel('Tutorial Group')
plt.ylabel('Number of times school repeated')
plt.title('Number of schools repeated per group')


#plot graph for gender imbalance
groups_with_gender_imbalance = []
for tutorialGroup in groups:

    for group_index in groups[tutorialGroup]:
        male_count = 0
        female_count = 0

        for student in groups[tutorialGroup][group_index]:
            if student[5] == 'Male':
                male_count += 1
            else:
                female_count += 1
        
        if male_count >= 4 or female_count >= 4:
            groups_with_gender_imbalance.append(f'{tutorialGroup} Group {group_index}')




# print(groups_with_duplicate_school)
plt.show()