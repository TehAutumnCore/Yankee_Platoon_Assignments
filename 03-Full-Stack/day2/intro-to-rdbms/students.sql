-- drawsql
-- https://drawsql.app/teams/franciscos-team-2-1/diagrams/yankee

DROP TABLE IF EXIST student; --if table exist, to drop it

CREATE TABLE student (   --create student table
    id SERIAL PRIMARY KEY, --creates a sequence db table that keeps count/increments
    first_name VARCHAR(50), --first_name variable as variable character
    last_name VARCHAR(50), --last_name variable as variable character
    age INT, --age variable as an int
    grade CHAR(1) --grade variable as a character variable
);

\COPY student FROM './students.csv' DELIMITER ',' CSV HEADER; --copy student info from csv s
-- INSERT INTO student(first_name,last_name,age,grade) VALUES --Insert data into data table
    -- ('John','Doe',18, 'A'),
    -- ('Jane','Smith',19,'B');

-- SELECT * FROM student; --select all from student
-- SELECT * FROM student_id_seq; --select all from student_id sequence

-- SELECT first_name, last_name FROM student;
-- SELECT first_name FROM student WHERE grade = 'B'; --grades only the first name from student where grades are equal to 'B'

-- SELECT COUNT(*) FROM student WHERE grade='B' --grabs the count/total amount of students who have a grade='b'

-- SELECT * FROM student ORDER BY last_name DESC; --selects all students by last name in descending order
-- SELECT first_name, age FROM student WHERE age between 18 and 20; --Select all first name and age from students where the age is between 18 and 20
-- SELECT first_name, age FROM student WHERE age between 18 and 20 limit 3; --Select all first name and age from students where the age is between 18 and 20 with a limit of only 3 names being returned

SELECT grade, COUNT(*) as grade_count FROM student GROUP BY grade --selects all the grades and the counts of each grade