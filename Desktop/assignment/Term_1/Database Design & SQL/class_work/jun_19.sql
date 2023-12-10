CREATE TABLE STUDENTMASTER(
ROLLNO NUMBER(4) PRIMARY KEY,
NAME VARCHAR2(10),
AGE NUMBER(2),
ADDRESS VARCHAR2(10)
);

CREATE TABLE STUDENTDETAILS(
ROLLNO NUMBER(4) REFERENCES STUDENTMASTER(ROLLNO),
SUBJECT VARCHAR2(10),
MARKS NUMBER(2)
);

INSERT INTO STUDENTMASTER
VALUES (1,'Peter',25,'Toronto');

INSERT INTO STUDENTMASTER
VALUES (2,'David',45,'Brampton');


INSERT INTO STUDENTDETAILS -- constraint violated
VALUES (3,'Maths',75);


DELETE FROM  STUDENTMASTER WHERE ROLLNO=2;  -- child record found

DELETE FROM  STUDENTMASTER WHERE ROLLNO=2; 

DELETE FROM  STUDENTDETAILS WHERE ROLLNO=2;
DELETE FROM  STUDENTMASTER WHERE ROLLNO=2;

--class activity
CREATE TABLE "EMPLOYEES" 
   (	"EMPLOYEE_ID" NUMBER(6,0), 
	"FIRST_NAME" VARCHAR2(20 BYTE), 
	"LAST_NAME" VARCHAR2(25 BYTE), 
	"EMAIL" VARCHAR2(25 BYTE), 
	"PHONE_NUMBER" VARCHAR2(20 BYTE), 
	"HIRE_DATE" DATE, 
	"JOB_ID" VARCHAR2(10 BYTE), 
	"SALARY" NUMBER(8,2), 
	"COMMISSION_PCT" NUMBER(2,2), 
	"MANAGER_ID" NUMBER(6,0), 
	"DEPARTMENT_ID" NUMBER(4,0)
   )


   SELECT first_name , last_name familyname, email FROM employees;


   SELECT first_name , last_name AS familyname, email FROM employees;


   SELECT first_name , last_name AS "family name", email FROM employees;

   SELECT first_name,salary,salary*1.10 AS " Increased Salary" FROM EMPLOYEES

   SELECT first_name,salary,salary*1.10 AS " Increased Salary" FROM EMPLOYEES

	SELECT first_name,salary,commission_pct,nvl(commission_pct,0)+salary FROM EMPLOYEES;

	select q'[I'm using quote operator in SQL statements]' as "Quote Operator" from dual;

select 'I'm using quote operator in SQL statements' as "Quote Operator" from dual;

SELECT distinct job_id FROM employees;
SELECT distinct first_name FROM employees;

SELECT unique job_id FROM employees;

SELECT distinct job_id, unique department_id FROM employees; 
SELECT distinct job_id FROM employees; 
SELECT distinct department_id FROM employees;

SELECT distinct job_id, department_id, first_name FROM employees;
SELECT job_id, distinct department_id, first_name FROM employees;

SELECT 'My Name is Sagara' FROM employees;
SELECT  first_name FROM employees;
SELECT 'My Name is ' || first_name FROM employees;
SELECT 'My Salary is ' || salary FROM employees;
SELECT 'My Salary is ' || salary AS "Salary Of Employees" FROM employees;
SELECT 'The commission percentage is ' || commission_pct AS concatenation,commission_pct FROM employees;
SELECT first_name || last_name  FROM employees;
SELECT first_name || ' ' || last_name ||' '|| salary AS "full name and salary" FROM employees;
SELECT * FROM employees;

SELECT * FROM employees;
SELECT employee_id, salary, salary*12 as annual_salary FROM employees;
SELECT employee_id, salary, salary+100*12 as annual_salary FROM employees; 
-this is not i want
SELECT employee_id, salary, (salary+100)*12 as annual_salary FROM employees;
SELECT sysdate FROM dual;
SELECT sysdate + 4 FROM dual;
SELECT employee_id, hire_date, hire_date+5 FROM employees;
SELECT salary, salary*commission_pct, commission_pct FROM employees;

SELECT * FROM employees;
SELECT employee_id, salary, salary*12 as annual_salary FROM employees;
SELECT employee_id, salary, salary+100*12 as annual_salary FROM employees; 
-this is not i want
SELECT employee_id, salary, (salary+100)*12 as annual_salary FROM employees;

SELECT sysdate FROM dual;
SELECT sysdate + 4 FROM dual;
SELECT employee_id, hire_date, hire_date+5 FROM employees;
SELECT salary, salary*commission_pct, commission_pct FROM employees;

SELECT sysdate FROM dual;
SELECT current_timestamp from dual;
SELECT sysdate + 7 FROM dual;
SELECT user FROM dual;

SELECT first_name, last_name FROM employees;

SELECT *  FROM employees 
WHERE salary > 10000;

SELECT * FROM employees 
WHERE job_id = 'IT_PROG';

alter session set nls_date_format = 'YYYY MM DD';
/
select sysdate from dual;

alter session set nls_date_format = 'YYYY MM DD';
/
select sysdate from dual;
ALT SESSION SET NLS-DATE-FORMAT 
SELECT * FROM employees WHERE hire_date > '2005-06-05';
SELECT * FROM employees WHERE hire_date = '2006-01-03';

SELECT * FROM employees WHERE salary BETWEEN 10000 AND 14000;

SELECT * FROM employees WHERE salary BETWEEN 14000 AND 10000;


select sysdate from dual;
select * from employees;
SELECT * FROM employees WHERE hire_date BETWEEN '2002-01-01' AND '2008-01-01';