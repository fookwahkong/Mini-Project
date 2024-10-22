
def arrangebySchool(records):
    '''
    This function serves the purpose of arranging the unsorted list of students by School

    Parameter:
    Input: Unsorted list of dictionaries
    Output: Lists of dictionaries in a list
    e.g.output = [
    'School 1': [{student 1, {student 2}, ...],  
    'School 2': [{student 1}, {student 2}, ...], 
    'School 3': [...], ...] 
    '''
    schools = {}
    record = []

    for student in records:
        school = student['School']

        if school not in schools.keys():
            schools[school] = []
        
        schools[school].append(student)

    return schools

def arrangebyGender(records):
    '''
    This function serves the purpose of arranging the list of students sorted by School 
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
    
    records.sort(key=lambda d: -d['CGPA'])
    return records

