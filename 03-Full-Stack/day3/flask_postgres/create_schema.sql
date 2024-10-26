--Schema
DROP TABLE IF EXISTS students;
CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    age integer,
    subject integer
)
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject varchar(255) NOT NULL
)
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    age integer,
    subject integer
)