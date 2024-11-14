--psql constrains_db < relationships.sql
--constraints_db
-- SELECT * FROM employees;
-- SELECT * FROM social_securies



--1 to 1 RELATIONSHIP because it has a unique forgein key
-- DROP TABLE IF EXISTS employees CASCADE; --CASCADE method says this table has a dependent

-- CREATE TABLE employees(
--     employee_id SERIAL PRIMARY KEY,
--     employee_name VARCHAR(100) NOT NULLL
-- );


-- DROP TABLE IF EXISTS social_securities;

-- CREATE TABLE social_securities(
--     ssn_id SERIAL PRIMARY KEY,
--     employee_id INT UNIQUE, --foreign key that will connect this table with the employees table 
--     ssn VARCHAR(11) UNIQUE NOT NULL,
--     FOREIGN KEY(employee_id) REFERENCES employees(employee_id) 
-- );
-- --will give an error since second table is dependent on the first table, since line 6 is trying to drop that table
-- INSERT INTO employees(employee) VALUES('Roger');
-- INSERT INTO social_securies(employee_id,ssn) VALUES (1, '222-22-2222');
-- INSERT INTO social_securies(employee_id,ssn) VALUES (1, '333-33-3333') --have to give employee id UNIQUE to prevent another ssn being assigned to an existing employee_id



one to many RELATIONSHIP because they share a foreign key
DROP TABLE IF EXISTS universities CASCADE;

CREATE TABLE universities(
    university_id SERIAL PRIMARY KEY,
    university_name VARCHAR(70) UNIQUE NOT NULL
);




DROP TABLE IF EXISTS students;

CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    university_id
    FOREIGN KEY(university_id) REFERENCES universities(university_id)
);

INSERT INTO universities(university_name) VALUES ('CODE PLATOON')
INSERT INTO students (student_name, university_id) 
VALUES 
('Sam', 1),
('Jesus', 1),
('Hailey', 1),
('Jacob', 1);

SELECT * FROM students JOIN universities ON students.university_id = universities.university_id WHERE UNIVERSITY = 1




--many to many relationship 
DROP TABLE IS EXISTS students CASCADE;

CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL
);


DROP TABLE IF EXISTS courses;

CREATE TABLE courses(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
);

DROP TABLE IF EXISTS course_students;

CREATE TABLE course_students(
        course_students SERIAL PRIMARY KEY,
        student_id INT,
        course_id INT,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO students(student_name) VALUES ('Tristan'),
INSERT INTO students(student_name) VALUES ('James'),
INSERT INTO students(student_name) VALUES ('Ryan'),
INSERT INTO students(student_name) VALUES ('Gary'),
INSERT INTO students(student_name) VALUES ('Jacob'),

INSERT INTO courses(course_name) VALUES('Python'),
INSERT INTO courses(course_name) VALUES('Javascript'),

--Connects through the primary key of both students
INSERT INTO course_students(student_id, course_id) VALUES(1,2),
INSERT INTO course_students(student_id, course_id) VALUES(2,1),
INSERT INTO course_students(student_id, course_id) VALUES(2,2),
INSERT INTO course_students(student_id, course_id) VALUES(3,1),
INSERT INTO course_students(student_id, course_id) VALUES(4,1),
INSERT INTO course_students(student_id, course_id) VALUES(5,1),
INSERT INTO course_students(student_id, course_id) VALUES(5,2),