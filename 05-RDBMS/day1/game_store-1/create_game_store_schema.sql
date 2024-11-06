DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id serial PRIMARY KEY,
    employee_name VARCHAR(255),
    position VARCHAR(255),
    salary DECIMAL(7,2)
);

DROP TABLE IF EXISTS posters;
CREATE TABLE posters (
    id serial PRIMARY KEY,
    poster_title VARCHAR(255),
    quantity INTEGER,
    price DECIMAL(4,2)
);

DROP TABLE IF EXISTS action_figures;
CREATE TABLE action_figures (
    id  serial PRIMARY KEY,
    action_figure_title VARCHAR(255),
    quantity INTEGER,
    price DECIMAL(4,2)
);

DROP TABLE IF EXISTS games;
CREATE TABLE games (
    game_id serial PRIMARY KEY,
    game_title VARCHAR(255),
    quantity INTEGER,
    price DECIMAL(4,2)
);