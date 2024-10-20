
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
