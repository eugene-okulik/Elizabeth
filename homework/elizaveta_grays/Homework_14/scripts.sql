INSERT INTO students (name,second_name) VALUES ('Elizaveta','Grays')

INSERT INTO books (title,taken_by_student_id) VALUES ('Master and Margarita', 23076)

INSERT INTO books (title,taken_by_student_id) VALUES ('War and World', 23076)

INSERT INTO books (title,taken_by_student_id) VALUES ('Evgenii Onegin', 23076)

INSERT INTO `groups` (id,title,start_date,end_date) VALUES (23076,'Tester', '01 aug 2026', '31 aug 2026')

INSERT INTO subjects (title) VALUES ('geography'), ('english'),('biology')


INSERT INTO lessons (title,subject_id) VALUES
('geography lesson 1', 23107),
('geography lesson 2', 23107),
('english lesson 1', 23108),
('english lesson 2', 23108),
('biology lesson1', 23109),
('biology lesson2', 23109)

INSERT INTO marks (value,lesson_id, student_id) VALUES
(5,76442,23076),
(4,76443,23076),
(3,15452 ,23076),
(3,15453, 23076),
(4,76446,23076),
(4,76447, 23076)

SELECT  value
FROM  marks
where student_id = 23076

SELECT title
from books
where taken_by_student_id = 23076

SELECT g.id, g.title, b.title, m.value , l.title , s2.title
from students s
join books b on s.id = b.taken_by_student_id
join marks m on s.id = m.student_id
join `groups` g on s.id = g.id
join lessons l on l.id = m.lesson_id
join subjects s2 on s2.id = l.subject_id
where s.id = 23076