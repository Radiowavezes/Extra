SELECT first_name as "First name", last_name as "Last name" from employees;
SELECT DISTINCT department_id from employees;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name, last_name, salary, salary*0.12 as PF FROM employees;
SELECT first_name, last_name, salary FROM employees WHERE salary = (SELECT MAX(salary) FROM employees) OR salary = (SELECT MIN(salary) FROM employees);
SELECT first_name, last_name, salary, ROUND((CAST(salary AS FLOAT)/12), 2) AS "Monthly salary" FROM employees;