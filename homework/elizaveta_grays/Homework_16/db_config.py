import dotenv
import csv
import os
import mysql.connector as mysql

dotenv.load_dotenv()

db_user = os.environ.get('DB_USER')
db_passw = os.environ.get('DB_PASSW')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')

db = mysql.connect(
    username=db_user,
    password=db_passw,
    host=db_host,
    port=db_port,
    database=db_name
)

cursor = db.cursor()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_csv_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_csv_path, newline='') as csvfile:
    file = csv.reader(csvfile)
    next(file)
    for row in file:
        cursor.execute(''' 
            select s.id
            from students s
            join `groups` g on s.group_id = g.id
            join books b on b.taken_by_student_id = s.id
            join marks m on m.student_id = s.id
            join lessons l on l.id = m.lesson_id  
            join subjects sub on sub.id = l.subject_id      
            where s.name = %s 
            and s.second_name = %s 
            and g.title = %s
            and b.title = %s 
            and sub.title = %s 
            and l.title = %s 
            and m.value = %s
            ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        if cursor.fetchone() is None:
            print(row)
