--FIRST CHALLANGE
SELECT * FROM CITY WHERE POPULATION>100000 AND COUNTRYCODE = "USA"

--SECOND CHALLANGE
--Query the NAME field for all American cities in the CITY table with populations larger than 120000. 
--The CountryCode for America is USA.

SELECT NAME FROM CITY WHERE POPULATION>120000 AND COUNTRYCODE = "USA"

--THIRD CHALLANGE
--Query all columns (attributes) for every row in the CITY table.
SELECT * FROM CITY;

--Query all columns for a city in CITY with the ID 1661.
SELECT * FROM CITY WHERE ID=1661;

--Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT * FROM CITY WHERE COUNTRYCODE = "JPN"

--Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT NAME FROM CITY WHERE COUNTRYCODE ="JPN"

--Query a list of CITY and STATE from the STATION table.
SELECT CITY,STATE FROM STATION 

--Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order,
-- but exclude duplicates from the answer.
--The STATION table is described as follows:
SELECT DISTINCT CITY FROM STATION  WHERE mod(ID,2)=0;

SELECT name FROM Employee ORDER BY name ASC;
--Write a query that prints a list of employee names (i.e.: the name attribute) for employees 
--in Employee having a salary greater than  per month who have been employees for less than  months. 
--Sort your result by ascending employee_id.

--Weather station start from 4
SELECT name FROM Employee WHERE salary > 2000 AND months <10 ORDER BY employee_id ASC;

--Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u)
-- as both their first and last characters. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY,1) IN ('a','e','i','o','u') AND RIGHT(CITY,1) IN ('a','e','i','o','u');

--Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u')

--Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) NOT IN ('a','e','i','o','u');

--Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels.
-- Your result cannot contain duplicates.
SELECT DISTINCT CITY 
FROM STATION 
WHERE LEFT(CITY,1) NOT IN ('A','E','I','O','U') OR RIGHT(CITY,1) NOT IN ('A','E','I','O','U');


--Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U') AND RIGHT(CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');



--Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters
-- of each name. If two or more students both have names ending in the same last three characters 
--(i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
SELECT Name
FROM Students
WHERE Marks > 75
ORDER BY RIGHT(Name, 3), Id;





--Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee 
--having a salary greater than  per month who have been employees for less than  months. 
--Sort your result by ascending employee_id.

SELECT name FROM Employee WHERE salary >2000 and months <10;


--Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

--Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'Asia'



--Query the total population of all cities in CITY where District is California.
SELECT sum(population) FROM CITY WHERE DISTRICT = 'California';

--Query the average population of all cities in CITY where District is California.
SELECT AVG(population) FROM CITY WHERE DISTRICT = "California"


--Query the average population for all cities in CITY, rounded down to the nearest integer.
SELECT ROUND(AVG(POPULATION),0) FROM CITY 