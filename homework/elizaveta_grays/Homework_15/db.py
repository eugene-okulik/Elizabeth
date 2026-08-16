import mysql.connector as mysql

db = mysql.connect(
    username='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Maria', 'Ivanova')
cursor.execute(query, values)
student_id = cursor.lastrowid
cursor.execute('SELECT id FROM students WHERE id = %s', (student_id,))
print(cursor.fetchone())
db.commit()

query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values = [
    ('Harry Potter', student_id),
    ('The Lord of the Rings', student_id),
    ('Sherlock Holmes', student_id)
]
cursor.executemany(query, values)
db.commit()

query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values = ('High Group', '13 jul 2026', '31 dec 2026')
cursor.execute(query, values)
group_id = cursor.lastrowid
cursor.execute('SELECT id FROM `groups` WHERE id = %s', (group_id,))
print(cursor.fetchone())
db.commit()

query = 'UPDATE students SET group_id = %s where id = %s'
values = (group_id, student_id)
cursor.execute(query, values)
db.commit()

query = 'INSERT INTO subjects (title) VALUES (%s)'
values = [('History',),
          ('Mathematic',),
          ('Literature',)
          ]
subject_ids = {}
for title in values:
    subject_name = title[0]
    cursor.execute(query, (subject_name,))
    subject_id = cursor.lastrowid
    subject_ids[subject_name] = subject_id
print(subject_ids)
db.commit()

query = 'INSERT INTO lessons (title,subject_id) VALUES(%s,%s)'
values = [
    ('Literature lesson 1', 'Literature'),
    ('Literature lesson 2', 'Literature'),
    ('Mathematic lesson 1', 'Mathematic'),
    ('Mathematic lesson 2', 'Mathematic'),
    ('History lesson 1', 'History'),
    ('History lesson 2', 'History')
]
lessons_to_insert = {}
for item in values:
    lesson_name = item[0]
    subject_name = item[1]
    subject_id = subject_ids[subject_name]
    cursor.execute(query, (lesson_name, subject_id,))
    lesson_id = cursor.lastrowid
    lessons_to_insert[lesson_name] = lesson_id
print(lessons_to_insert)

db.commit()

query = 'INSERT INTO marks (value,lesson_id, student_id) VALUES (%s, %s, %s)'
values = [
    (5, 'Literature lesson 1', student_id),
    (3, 'Literature lesson 2', student_id),
    (4, 'Mathematic lesson 1', student_id),
    (3, 'Mathematic lesson 2', student_id),
    (5, 'History lesson 1', student_id),
    (5, 'History lesson 2', student_id)
]
cursor.executemany(query, values)
db.commit()

cursor.execute('SELECT value FROM marks where student_id = %s', (student_id,))
print(cursor.fetchall())

cursor.execute('SELECT title from books where taken_by_student_id = %s', (student_id,))
print(cursor.fetchall())

cursor = db.cursor(dictionary=True)
query = ''' SELECT g.id, g.title, b.title, m.value , l.title , s2.title
    from students s
    join books b on s.id = b.taken_by_student_id
    join marks m on s.id = m.student_id
    join `groups` g on g.id = s.group_id
    join lessons l on l.id = m.lesson_id
    join subjects s2 on s2.id = l.subject_id
    where s.id = %s
    '''
cursor.execute(query, (student_id,))
print(cursor.fetchall())

cursor.close()
db.close()
