def arrangebySchool(records):
    '''
    This function serves the purpose of arranging the unsorted list of students by School

    Parameter:
    Input: Unsorted list of dictionaries

    Output: Lists of dictionaries in a list

    e.g. schools = [
    'School 1': [{student 1, {student 2}, ...],  
    'School 2': [{student 1}, {student 2}, ...], 
    'School 3': [...], ...] 
    '''
    schools = {}

    for student in records:
        school = student['School']

        if school not in schools.keys():
            schools[school] = []
        
        schools[school].append(student)

    return schools

def arrangebyGender(records):
    '''
    This function serves the purpose of arranging the unsorted list of students by Gender

    Parameter:
    Input: Unsorted list of dictionaries
    Output: Lists of dictionaries in a list

    e.g. record = {'Male': [{student 1}, {student 2}, ...], 
                    'Female': [{student 1}, {student 2}, ...]}
    '''
    males = []
    females = []

    for student in records:
        gender = student['Gender']

        if gender == 'Male':
            males.append(student)
        else:
            females.append(student)
    
    record = {'Male': males,
              'Female': females}
    
    return record 

def arrangebyGPA(records):
    '''
    This function serves the purpose of arranging the unsorted list of students by Gender

    Parameter:
    Input: Unsorted list of dictionaries
    Output: Sorted list of dictionaries

    e.g. records = [{student with highest GPA}, 
                    {student with second highest GPA}, 
                    ..., 
                    {student with lowest GPA}]
    '''

    records.sort(key=lambda x:x['CGPA'], reverse=True)
    return records

def assign_to_groups_focus_gender(students, num_groups=10):
    '''
    This function serves the purpose of grouping the list of students into groups while accounting 
    for focusing more on the diversity in Gender and GPA in each group

    Parameter:
    Input: Unsorted list of dictionaries, (Optional) Number of groups required
    Output: Sorted list of dictionaries

    groups = {1: [{student 1}, {student 2}, {student 3}, ...],
              2: [{student 1}, {student 2}, ...],
              ...}    
    '''

    groups = {i:[] for i in range(num_groups)}
    group_details = {i: {'Gender': {'Male': 0, 'Female': 0}, 'School':[], 'Size': 0} for i in range(num_groups)}

    # To make sure the diveristy of GPA in each group
    students = arrangebyGPA(students)
    group_size = len(students) // num_groups
    
    for i in range(group_size):
        groups_to_add = [i for i in range(num_groups)]

        for group_index in range(num_groups):
            
            student = students.pop(0)
            assigned = False
            
            valid = is_student_valid(student, group_index, group_details, group_size, groups_to_add)

            if valid:
                        
                groups[group_index].append(student)
                        
                # Update group_details
                group_details = update_details(group_index, group_details, student)
                groups_to_add.remove(group_index)

                assigned = True

            # if not assigned, iterate through the groups next in line 
            if not assigned:
                
                new_group_index = find_desired_group(student, group_index, group_details, group_size, groups_to_add)

                groups[new_group_index].append(student)

                #update group_details
                group_details = update_details(new_group_index, group_details, student)
                groups_to_add.remove(new_group_index)

                assigned = True

        students.reverse()

    return groups

def assign_to_groups_focus_school(students, num_groups=10):
    students = arrangebyGPA(students)

    group_size = 5

    groups = {i: [] for i in range(1, num_groups + 1)} #Makes X number of groups (lists) based on requirement
    
    group_details = {i: {'Gender': {'Male': 0, 'Female': 0}, 'School':[], 'Size': 0} for i in range(1, num_groups + 1)}

    distribute_students_prioritize_school(groups, students, group_details, group_size)
    distribute_remaining_students_prioritize_gender(groups, students, group_details, group_size)
    distribute_remaining_students(groups, students, group_details, group_size)

    return groups

def find_desired_group(student, group_index, group_details, group_size, groups_to_add):
    '''
    This function serves the purpose of finding the desired group for leftover student,
    sacrificing the diversity of school

    Parameters:
    Input:

    Output: desired group_index
    '''

    num_groups = len(group_details)
    gender = student['Gender']

    for new_group_index in range(group_index + 1, num_groups):
        if new_group_index in groups_to_add:
            if group_details[new_group_index]['Size'] < group_size:
                if group_details[new_group_index]['Gender'][gender] < group_size // 2:
                    return new_group_index
    
    for new_group_index in range(0, group_index):
        if new_group_index in groups_to_add:
            if group_details[new_group_index]['Size'] < group_size: 
                if group_details[new_group_index]['Gender'][gender] < group_size // 2:
                    return new_group_index

    # if unable to find the desired group, append to the most appropriate group
    # by comparing which group has the lowest number of that gender
    groups_to_compare = {}
    for group_index in groups_to_add:
        groups_to_compare[group_index] = group_details[group_index]

    new_group_index = smallest_num(groups_to_compare, gender)

    return new_group_index
    

def smallest_num(groups_to_compare, gender):
    '''
    This function serves the purpose of finding the group that has the smallest number of the specific gender
    '''
    
    smallest_male = 99999
    smallest_female = 99999
    
    for group_index in groups_to_compare.keys():

        if groups_to_compare[group_index]['Gender']['Male'] < smallest_male:
            
            smallest_male = groups_to_compare[group_index]['Gender']['Male']
            group_smallest_male = group_index

        if groups_to_compare[group_index]['Gender']['Female'] < smallest_female:
            smallest_female = groups_to_compare[group_index]['Gender']['Female']
            group_smallest_female = group_index
    
    
    if gender == 'Male':
        return group_smallest_male
    else:
        return group_smallest_female


def update_details(group_index, group_details, student):
    '''
    This function serves the purpose of updating the group_details

    Parameter:
    Input

    Output:
    None
    '''

    gender = student['Gender']
    school = student['School']

    group_details[group_index]['Gender'][gender] += 1
    group_details[group_index]['School'].append(school)
    group_details[group_index]['Size'] += 1

    return group_details

def is_student_valid(student, group_index, group_details, group_size, groups_to_add):
    '''
    This function serves the purpose of checking if the student is able to fit into the allocated group_index

    Parameter:
    Input:

    Output:
    True: if the student can be fitted into the group
    False: if the student cannot be fitted into the group
    '''

    gender = student['Gender']
    school = student['School']
    
    if group_index in groups_to_add:

        # Make sure that the group is not full
        if group_details[group_index]['Size'] < group_size:
            
            #Check if the number of 'gender' in the group is more than half of the group_size
            if group_details[group_index]['Gender'][gender] < group_size // 2: 
                
                # Check if there is duplicate school in the group
                if school not in group_details[group_index]['School']:
                    return True
            
    return False

def is_group_valid(student, group_index, group_details, group_size):

    max_amount = group_size // 2

    # Case 1: if the student is Male, and the group appending already has maximum male students, skip

    if (group_details[group_index]['Gender']['Male'] == max_amount) and (group_details[group_index]['Gender']['Female'] < max_amount):
        if student['Gender'] == 'Male':
            return False
        
    # Case 2: if the student is Female, and the group appending already has maximum female students, skip

    if (group_details[group_index]['Gender']['Female'] == max_amount) and (group_details[group_index]['Gender']['Male'] < max_amount):
        if student['Gender'] == 'Female':
            return False
    
    return True

def distribute_students_prioritize_school(groups, all_students, group_details, group_size):
    duplicate_schools = False

    while all_students and (not duplicate_schools):

        not_appended = 0  # Count how many times in the for-loop which resulted in nothing happening/ no appending. If count goes to = len(groups), 
                          # means that nothing can append anymore currently
        for group_index in range(1,len(groups)+1): #Loops through the groups
            total_students_before = len(all_students)  # Amount of students before appending process for each group
            if len(groups[group_index]) < group_size: #If group not filled
                #Start appending from the top GPA student after sorting GPA in descending order
                for index, student in enumerate(all_students):
                    
                    valid = is_group_valid(student, group_index, group_details, group_size)

                    if not valid:
                        continue

                    #Checks for no duplicate schools when either, 1) female and male count both < 2, meaning can append any gender, or 
                                                                # 2) female and male count both == 2, meaning can append any gender for the 5th member resulting in 3-2 ratio
                    if student['School'] not in group_details[group_index]['School']:
                        if student['Gender'] == 'Male':
                            update_details(group_index, group_details, student)
                        else:
                            update_details(group_index, group_details, student)
                        groups[group_index].append(all_students.pop(index)) #Append and pop student of index
                        break #Break out of for loop because we are done appending one from the top GPA
                    else:
                        continue

                #If reach required teamsize, break out of the loop and go to the next group
                if len(groups[group_index]) == group_size:
                    continue

                #Continue appending from the bottom GPA student after sorting GPA in descending order with the same appending algorithm as above
                for index, student in enumerate(reversed(all_students)): #Reverse iteration so we can iterate from the bottom 
                    valid = is_group_valid(student, group_index, group_details, group_size)
                    
                    if not valid:
                        continue

                    if student['School'] not in group_details[group_index]['School']:
                        if student['Gender'] == 'Male':
                            update_details(group_index, group_details, student)
                        else:
                            update_details(group_index, group_details, student)
                            
                        #Calculate the actual index of the student we are currently looking at because (index) and (actual_index) are looking at 2 diff pos in the list
                        actual_index = len(all_students) - 1 - index
                        groups[group_index].append(all_students.pop(actual_index))
                        break
                    else:
                        continue
            #Check if nobody gets appended during this iteration of the group (means that students left in all_students have duplicate school with someone currently in the group)
            total_students_after = len(all_students)
            if total_students_after == total_students_before:
                not_appended += 1  # Shows how many times or groups out of len(groups) that there was no appending/ no unqiue schools to append

        if not_appended == len(groups):  # All the groups are skipped because of the potential in duplicate school if appended
            duplicate_schools = True

def distribute_remaining_students_prioritize_gender(groups, all_students, group_details, group_size):
    #Exact same appending algorithm as (distribute_students_prioritize_school()), just with allowing duplciate schools, but still continue to distribute gender evenly
    duplicate_schools = False
    
    while all_students and not duplicate_schools:
        not_appended = 0

        for group_index in range(1,len(groups)+1):  
            total_students_before = len(all_students)
            if len(groups[group_index]) < group_size:
                for index, student in enumerate(all_students):
                    valid = is_group_valid(student, group_index, group_details, group_size)

                    if not valid:
                        continue

                    if student['Gender'] == 'Male':
                        update_details(group_index, group_details, student)
                        groups[group_index].append(all_students.pop(index))
                        break

                    if student['Gender'] == 'Female':
                        update_details(group_index, group_details, student)
                        groups[group_index].append(all_students.pop(index))
                        break

                if len(groups[group_index]) == group_size:
                    continue

                for index, students in enumerate(reversed(all_students)):
                    actual_index = len(all_students) - 1 - index
                    
                    valid = is_group_valid(student,group_index, group_details, group_size)
                    
                    if not valid:
                        continue

                    if students['Gender'] == 'Male':
                        update_details(group_index, group_details, student)
                        groups[group_index].append(all_students.pop(actual_index))
                        break

                    if students['Gender'] == 'Female':
                        update_details(group_index, group_details, student)
                        groups[group_index].append(all_students.pop(actual_index))
                        break

            total_students_after = len(all_students)
            if total_students_after == total_students_before:
                not_appended += 1

        if not_appended == len(groups):
            duplicate_schools = True

def distribute_remaining_students(groups, all_students, group_details, group_size):
    #Appending algorithm to distribute the rest of the students without distributing school and gender evenly because it has been distributed as well as it could already
    while all_students:
        for group_index in range(1,len(groups)+1):
            # Appends the rest of the students with duplicate schools into groups not filled
            if len(groups[group_index]) < group_size and all_students:
                student = all_students.pop(0)
                groups[group_index].append(student)  # Appends and pops the student with the highest GPA out of the remaining students
                update_details(group_index, group_details, student)
            else:
                continue
