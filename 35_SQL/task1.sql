SELECT first_name, last_name, employees.department_id, departments.depart_name FROM employees 
JOIN departments ON departments.department_id = employees.department_id;

SELECT first_name, last_name, department.department_name, locations.city, locations.state_province FROM employees
JOIN department ON employees.department_id = department.department_id
JOIN locations ON department.location_id = locations.location_id

SELECT first_name, last_name, department.department_id, department.department_name FROM employees 
JOIN department ON employees.department_id = department.department_id
WHERE department.department_id = 40 OR department.department_id = 80;

SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name FROM department
LEFT JOIN employees ON department.department_id = employees.department_id;

SELECT a.first_name as Employee, b.first_name as Manager FROM employees AS a
LEFT JOIN employees AS b ON a.manager_id = b.employee_id;

SELECT jobs.job_title as "Job title", (employees.first_name || " " || employees.last_name) AS "Full name", (jobs.max_salary - employees.salary) AS Difference
FROM employees
JOIN jobs on jobs.job_id = employees.job_id;

SELECT jobs.job_title AS "Job title", CAST(AVG(employees.salary) AS INTEGER) AS Average
FROM jobs
JOIN employees ON jobs.job_id = employees.job_id
GROUP BY jobs.job_title;

SELECT (employees.first_name || " " || employees.last_name) AS "Full name", employees.salary
FROM employees
JOIN department ON department.department_id = employees.department_id
JOIN locations ON department.location_id = locations.location_id
WHERE locations.city = 'London';

SELECT departments.depart_name as "Depart name", COUNT(*) AS Ammount
FROM departments
JOIN employees ON departments.department_id = employees.department_id
GROUP BY departments.depart_name;
