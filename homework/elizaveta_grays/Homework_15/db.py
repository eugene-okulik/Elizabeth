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
cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
print(cursor.fetchone())
db.commit()

query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values = [
    ('Harry Potter', 23078),
    ('The Lord of the Rings', 23078),
    ('Sherlock Holmes', 23078)
]
cursor.executemany(query, values)
db.commit()

query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values = ('High Group', '13 jul 2026', '31 dec 2026')
cursor.execute(query, values)
group_id = cursor.lastrowid
cursor.execute(f'SELECT * FROM `groups` WHERE id = {group_id}')
print(cursor.fetchone())
db.commit()

query = 'UPDATE students SET group_id = %s where id = %s'
values = (23079, 23078)
cursor.execute(query, values)
db.commit()

query = 'INSERT INTO subjects (title) VALUES (%s)'
values = [('History',),
          ('Mathematic',),
          ('Literature',)
          ]
cursor.executemany(query, values)
cursor.execute(
    "SELECT * FROM subjects WHERE title IN (%s, %s, %s) ORDER BY id DESC LIMIT 3",
    ('History', 'Mathematic', 'Literature'))
print(cursor.fetchall())
db.commit()

query = 'INSERT INTO lessons (title,subject_id) VALUES(%s,%s)'
values = [
    ('Literature lesson 1', 23121),
    ('Literature lesson 2', 23121),
    ('Mathematic lesson 1', 23120),
    ('Mathematic lesson 2', 23120),
    ('History lesson 1', 23119),
    ('History lesson 2', 23119)
]
cursor.executemany(query, values)
cursor.execute(
    "SELECT id, title FROM lessons WHERE title IN (%s, %s, %s,%s, %s, %s) ORDER BY id DESC LIMIT 6",
    ('Literature lesson 1', 'Literature lesson 2', 'Mathematic lesson 1', 'Mathematic lesson 2',
     'History lesson 1', 'History lesson 2'))
print(cursor.fetchall())
db.commit()

query = 'INSERT INTO marks (value,lesson_id, student_id) VALUES (%s, %s, %s)'
values = [
    (5, 76452, 23078),
    (3, 76453, 23078),
    (4, 76451, 23078),
    (3, 76450, 23078),
    (5, 76449, 23078),
    (5, 76448, 23078)
]
cursor.executemany(query, values)
db.commit()

cursor.execute('SELECT value FROM marks where student_id = %s', (23078,))
print(cursor.fetchall())

cursor.execute('SELECT title from books where taken_by_student_id = %s', (23078,))
print(cursor.fetchall())

cursor = db.cursor(dictionary=True)
query = ''' SELECT g.id, g.title, b.title, m.value , l.title , s2.title
    from students s
    join books b on s.id = b.taken_by_student_id
    join marks m on s.id = m.student_id
    join `groups` g on g.id = s.group_id
    join lessons l on l.id = m.lesson_id
    join subjects s2 on s2.id = l.subject_id
    where s.id = 23078
    '''
cursor.execute(query)
print(cursor.fetchall())

db.close()
