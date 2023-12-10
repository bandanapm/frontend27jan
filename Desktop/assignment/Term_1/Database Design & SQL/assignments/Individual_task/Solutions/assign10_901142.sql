--1
CREATE VIEW myView_142 AS
SELECT employee_id, first_name, last_name, department_id
FROM employees;

--2
SELECT * FROM user_views WHERE view_name = 'MYVIEW_142';

--3
SELECT * FROM myView_142;
