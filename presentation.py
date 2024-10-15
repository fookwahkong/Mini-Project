import matplotlib as mpl
import matplotlib.pyplot as plt

with open('groups.csv','r') as f:
    header = f.readline().strip().split(',')

    students = f.readlines()

    groups = {}
    for student in students:
        student = student.strip().split(',')
        
        group_idx = student[0] 
        if group_idx not in groups.keys():
            groups[group_idx] = [] 

        groups[group_idx].append(student)
        

#test
schools_avgNum = {}
groups_avgGPA = {}

for group_idx in groups:

    #initialising variables to find mean GPA for each group
    no_of_students = 0
    total = 0

    for student in groups[group_idx]:

        #to find the number of students from each school in a group
        if student[3] not in schools_avgNum[group_idx].keys():   #index 3 is the postion of school name in the list
            schools_avgNum[group_idx] = {student[3]:0}

        schools_avgNum[group_idx][student[3]] += 1 
        

        #to find mean GPA for each group
        GPA = float(student[6])                      #index 6 is the position of GPA in the list
        no_of_students += 1
        total += GPA 

    averageGPA = round(total / no_of_students, 2)
    groups_avgGPA[group_idx] = averageGPA

# Plot graph for the number of students from each school in a group
print(schools_avgNum)

# to find the mean value
for group_idx in groups:
    for student in groups[group_idx]:
        total += float(student[6])
mean = total / 6000

# Plot graph for GPA
groups_index = list(groups_avgGPA.keys())
groupAverageGPA = list(groups_avgGPA.values())
plt.figure(figsize=(200, 10))
plt.bar(groups_index, groupAverageGPA, color='skyblue')

# Adding labels and title
plt.xlabel('Group')
plt.ylabel('Average GPA')
plt.title('Average GPA per Group')

# Adding horizontal average line
plt.axhline(mean, color='red', linestyle='--')

# Show the plot
plt.show()
    