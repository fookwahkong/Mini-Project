with open('new_records.csv','r') as f:
    header = f.readline().strip().split(',')
    file = f.readlines()

    records = []

    for student in file:
        student = student.strip().split(',')  # to change str to a list of strings
        record = {}
        
        for i in range(len(student)):
            record[header[i]] = student[i]

        
        records.append(record)

for line in records:
    print(line)