
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

def assign_to_groups(students, num_groups=10):
    '''
    This function serves the purpose of grouping the list of students into groups while accounting 
    for diversity in School, Gender and GPA in each group

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
            
            valid = is_valid(student, group_index, group_details, group_size, groups_to_add)

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

def is_valid(student, group_index, group_details, group_size, groups_to_add):
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