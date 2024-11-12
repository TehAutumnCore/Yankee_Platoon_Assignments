# load 

CREATE DATABASE car_shop_db;
\c car_shop_db
psql <database name>  <  <file_name>



\d shows all the relations from within the db
car_id_seq keeps count of the last value stores in car_id

SELECT * FROM car;
SELECT * FROM car_id_seq;

SELECT * from car;

SELECT obj_description('car'::regclass); 
<!-- grabs comments from table 'car':: register classes(table)  -->


SELECT * FROM car 

EXPLAIN SELECT * FROM car WHERE year >= 2019; <!-- tells you how the filter/query works-->
EXPLAIN ANALYZE SELECT * FROM car WHERE year >= 2019; <!-- tells you how the filter/query works, as well as the runtime, what was filtered out/removed -->
SELECT COUNT(*) FROM car; <!-- 10 -->
SELECT COUNT(*) FROM car WHERE color = 'Red'; <!-- 2 -->

SELECT SUM(price) FROM services; <!-- returns a column with the suum of prices from services table -->
SELECT AVG(salary) FROM employees; <!-- returns the average of the employees salaries from the employee table -->
SELECT ROUND(AVG(salary),2) FROM employees; <!-- returns the average of the employees salaries from the employee table rounded -->
SELECT * FROM driver WHERE name LIKE '%JOHNSON';
SELECT * FROM driver WHERE name LIKE '%example.com'; <!-- returns all drivers with an email like example.com -->
SELECT * FROM employees WHERE first_name like 'J%' <!--  -->
SELECT * FROM plate WHERE plate_number LIKE '%X%';
SELECT * FROM plate WHERE plate_number LIKE '%x%';
SELECT * FROM car WHERE color IN ('Red','White','Blue');
SELECT * FROM car WHERE year IN (2017,2020,2022);
SELECT sum(price) AS complete_service_cost FROM services;

SELECT name_of_service, price AS service_cost FROM services;
SELECT name_of_service AS service, price AS service_cost FROM services;
SELECT * FROM car LIMIT 3; <!-- limits to the first 3 -->
SELECT * FROM car
SELECT * FROM car ORDER BY model;
SELECT * FROM car ORDER BY model DESC;
SELECT * FROM car ORDER BY model DESC LIMIT 3;
SELECT make, COUNT(*) FROM car GROUP BY make; 
SELECT make FROM car GROUP BY make;

SELECT year, COUNT(*) FROM car GROUP BY year;
SELECT year, COUNT(*) FROM car GROUP BY year ORDER BY year DESC LIMIT 3;

<!-- returns low, medium or high depending -->
SELECT CASE WHEN PRICE < 30 THEN 'Low'
WHEN PRICE < 50 THEN 'Medium'
ELSE 'High'
END AS price_range
from services;

SELECT price FROM services;
SEELCT price AS price_range FROM services
SELECT car.*, driver.* FROM car JOIN driver ON car.driver = driver.id;
SELECT c.*, d.* FROM car c JOIN d ON c.driver = d.id;
<!-- above is grabbing all columns from c or car while below is specifying just the make, model, name -->
SELECT car.make, car.model, driver.name FROM car c JOIN driver ON car.driver = driver.id;
SELECT c.*, d.* FROM car c JOIN d ON c.driver = d.id ORDER BY driver.age;
SELECT c.*, d.* FROM car c JOIN d ON c.driver = d.id ORDER BY d.age DESC;
SELECT c.*, d.* FROM car c JOIN d ON c.driver = d.id ORDER BY d.age DESC LIMIT 3;
SELECT c.*, d.name, d.age FROM car c LEFT JOIN driver d ON c.driver = driver.id;
SELECT c.*, d.name, d.age FROM car c RIGHT JOIN d ON c.driver = d.id

SELECT c.make, c.model, c.year, s.name_of_service AS service, s.price
FROM car_service
JOIN services s ON car_service.service_id = s.id
JOIN car c ON car_service.car_id = c.id