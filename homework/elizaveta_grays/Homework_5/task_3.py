students = ['Ivanov', 'Petrov', 'Sidorov']
last_name1, last_name2, last_name3 = students

subjects = ['math', 'biology', 'geography']
subject1, subject2, subject3 = subjects

students = ', '.join(students)
subjects = ', '.join(subjects)

print('Students ' + students + 'study these subjects: ' + subjects)
