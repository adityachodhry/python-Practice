CREATE TABLE IF NOT EXISTS student(
s_id INT PRIMARY KEY, 
s_name VARCHAR(50), 
s_section VARCHAR(5), 
s_marks BOOLEAN NOT NULL
);

SELECT * FROM student; 

INSERT INTO student (s_id, s_name, s_section, s_marks)  
VALUES  
(1, 'Aditya', 'A', 90),  
(2, 'Rahul', 'B', 85),  
(3, 'Sneha', 'A', 92),  
(4, 'Vikram', 'C', 88),  
(5, 'Priya', 'B', 95);

USE practice;

UPDATE student
SET s_marks = 70
WHERE s_id = 5;

ALTER TABLE student
ADD COLUMN sub_name VARCHAR(50);

UPDATE student SET sub_name = 'Math' WHERE s_id = 1;
UPDATE student SET sub_name = 'Chem' WHERE s_id = 2;
UPDATE student SET sub_name = 'Phy' WHERE s_id = 3;
UPDATE student SET sub_name = 'Math' WHERE s_id = 4;
UPDATE student SET sub_name = 'Chem' WHERE s_id = 5;

SELECT s_id, sub_name FROM student;

SELECT * FROM student;

SELECT s_name, s_marks FROM student
WHERE s_marks >= 90;

SELECT * FROM student
WHERE s_section = "A";

SELECT COUNT(*) FROM student
WHERE s_section = "B";

SELECT AVG(s_marks) FROM student;
SELECT AVG(s_marks) As avg_marks FROM student;

SELECT s_id, s_name FROM student
WHERE sub_name = "Math";

SELECT * From student;

SELECT * FROM student 
ORDER BY s_marks ASC;

SELECT * FROM student 
ORDER BY s_marks DESC LIMIT 3;

SELECT * FROM student
WHERE s_marks = (SELECT MAX(s_marks) FROM student);

SELECT s_section, COUNT(*) AS num_of_Student FROM Student
GROUP BY s_section;

SELECT * FROM student
WHERE s_marks BETWEEN 80 AND 90;

SELECT * FROM student 
WHERE s_name LIKE 'A%';

SELECT sub_name, COUNT(*) AS total_num_of_student FROM student
GROUP BY sub_name;

SELECT s_id, s_name, s_marks, RANK() OVER (ORDER BY s_marks DESC) AS student_rank
FROM student;

SELECT * FROM student
WHERE sub_name = (SELECT sub_name FROM student 
WHERE s_name = 'Aditya');

SELECT * FROM student;
SET SQL_SAFE_UPDATES = 0;

UPDATE student 
SET sub_name = 'Biology' 
WHERE s_section = 'B';

SELECT * 