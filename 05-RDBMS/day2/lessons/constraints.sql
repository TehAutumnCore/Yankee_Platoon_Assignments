--createdb constraints
--psql constraints < constraints.sql


-- DROP TABLE IF EXISTS students;

-- CREATE TABLE students(
--     student_id SERIAL PRIMARY KEY, --UNIQUE, incrementing NOT repeating
--     student_name VARCHAR(100), --type string, max chars 100
--     student_email VARCHAR(255) UNIQUE
-- );

-- INSERT INTO students(student_name,student_email) VALUES ('james','james@james.com')
-- INSERT INTO students(student_name,student_email) VALUES ('gary','gary@gary.com')

-- DROP TABLE IF EXISTS moves

-- CREATE TABLE movies(
--     movie_id SERIAL PRIMARY KEY,
--     movie_name VARCHAR(255) UNIQUE CHECK(movie_name ~ '^[A-Z][a-z]*$'),
--     -- age_limit INT CHECK (age_limit BETWEEN 0 AND 18) --age_limit BETWEEN 0 AND 18
--     age_limit INT CHECK (age_limit IN (13, 15, 18)) --age_limit >= 0 and age_limit <= 18
--     CHECK(movie_name ~ '^[A-Z][a-z]*$') -- can also be used outside, so its not limited to just that field 
--);

-- INSERT INTO movies(movie_name,age_limit) VALUES ('Python',15)
-- INSERT INTO movies(movie_name,age_limit) VALUES ('It',21)

-- DROP TABLE IF EXISTS product;

-- CREATE TABLE product(
--     product id SERIAL PRIMARY KEY,
--     product_name VARCHAR(100) UNIQUE NOT NULL, --NOT NULL means it cant be empty, requires input for field
--     -- quantity INT CHECK (quantity >= 0) DEFAULT 0       --can use a check, and DEFAULT 0
--     quantity INT CHECK (quantity > 0)
-- );

-- INSERT INTO product(product_name, quantity) VALUES('grill cheese makers',0)




DROP TABLE IF EXISTS games;

CREATE TABLE IF EXISTS games(
    game_id SERIAL PRIMARY KEY,
    --unique,regex, not null
    game_title VARCHAR(50) UNIQUE NOT NULL
    CHECK(game_title ~ '^[A-Za-z09 _\-:''\\]'),
    --greater orr equal to 0 - 100 not null default 0
    quantity INTEGER NOT NULL 
    --greater or equal to 0 less than or equal to 69.99
    price DECIMAL(4,2) 
    CHECK(quantity BETWEEN 0 and 100) DEFAULT 0, 
    CHECK(price BETWEEN 0 AND 69.99) DEFAULT 10
)

\COPY games FROM '..data/game.csv' WITH CSV HEADER;