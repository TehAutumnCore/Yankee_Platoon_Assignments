-- Employee Seed Data
-- COPY employees(id,employee_name,position,salary) FROM '/home/desktop/yankee_platoon/05-RDBMS/day1/game_store-1/csv/employee.csv'
-- DELIMITER ','
-- CSV HEADER;

INSERT INTO employees(id, employee_name, position, salary) VALUES
(1, 'John Doe', 'Sales Associate', 40000.00);
(2, 'Jane Smith', 'Store Manager', 60000.00);
(3, 'Mark Johnson', 'Inventory Clerk', 35000.00);
(4, 'Emily Davis', 'Customer Service Representative', 38000.00);
(5, 'Chris Wilson', 'IT Specialist', 55000.00);
(6, 'Anna Brown', 'Marketing Coordinator', 45000.00);
(7, 'Michael Lee', 'Assistant Manager', 52000.00);
(8, 'Sarah Miller', 'Finance Analyst', 48000.00);
(9, 'David Garcia', 'Security Officer', 32000.00);
(10, 'Lisa Taylor', 'HR Coordinator', 42000.00);

-- Posters Seed Data
-- COPY posters(id, poster_title, quantity, price) FROM '/home/desktop/yankee_platoon/05-RDBMS/day1/game_store-1/csv/posters.csv'
-- DELIMITER ','
-- CSV HEADER;

INSERT INTO posters(id, poster_title, quantity, price) VALUES
(1, 'Movie Poster', 1, 15.99);
(2, 'Game Poster', 1, 7.99);
(3, 'Superhero Poster', 1, 12.99);
(4, 'Anime Poster', 1, 8.99);
(5, 'Music Poster', 1, 6.99);
(6, 'TV Series Poster', 1, 10.99);
(7, 'Sci-Fi Poster', 1, 11.99);
(8, 'Fantasy Poster', 1, 14.99);
(9, 'Cartoon Poster', 1, 6.49);
(10, 'Sports Poster', 1, 9.49);

-- Action Figure Seed Data
-- COPY action_figures(id, action_figure_title, quantity, price) FROM '/home/desktop/yankee_platoon/05-RDBMS/day1/game_store-1/csv/action_figure.csv'
-- DELIMITER ','
-- CSV HEADER;

INSERT INTO action_figures(id, action_figure_title, quantity, price) VALUES
(1, 'Superhero Figure', 1, 19.99);
(2, 'Game Character Figure', 1, 24.99);
(3, 'Anime Character Figure', 1, 29.99);
(4, 'Sci-Fi Character Figure', 1, 22.99);
(5, 'Fantasy Character Figure', 1, 27.99);
(6, 'Movie Character Figure', 1, 23.49);
(7, 'Cartoon Character Figure', 1, 18.99);
(8, 'Military Figure', 1, 21.99);
(9, 'Sports Figure', 1, 17.49);
(10, 'Historical Figure', 1, 26.49);

-- Game Seed Data
-- COPY games(game_id, game_title, quantity, price) FROM '/home/desktop/yankee_platoon/05-RDBMS/day1/game_store-1/csv/game.csv'
-- DELIMITER ','
-- CSV HEADER;

INSERT INTO games(game_id, game_title, quantity, price) VALUES
(1, 'The Witcher 3: Wild Hunt', 30, 39.99);
(2, 'Grand Theft Auto V', 25, 49.99);
(3, 'Assassin''s Creed Valhalla', 20, 59.99);  -- Escaped single quote in 'Assassin's'
(4, 'Cyberpunk 2077', 15, 54.99);
(5, 'Red Dead Redemption 2', 35, 44.99);
(6, 'FIFA 22', 40, 29.99);
(7, 'Call of Duty: Warzone', 18, 39.99);
(8, 'Minecraft', 50, 19.99);
(9, 'Overwatch', 22, 34.99);
(10, 'Final Fantasy VII Remake', 28, 49.99);