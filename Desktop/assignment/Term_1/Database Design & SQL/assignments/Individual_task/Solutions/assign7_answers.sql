--1
SELECT 
  INITCAP(firstname),
  INITCAP(lastname)
FROM
  Customers;
--2
SELECT
    Customer# AS roshan_customer, 
    CASE
        WHEN Referred IS NULL THEN 'NOT REFERRED'
        ELSE 'REFERRED' 
        END AS ReferralStatus
FROM Customers;
--3
SELECT
    Title AS roshan_Title,
    ROUND (((Retail - Cost) / Cost) * 100) AS MarkupPercentage 
FROM Books;
--4
SELECT
    TO_CHAR (SYSDATE, 'Day') AS Roshan_CurrentDayOfWeek, 
    TO_CHAR (SYSDATE, 'HH24') AS Roshan_CurrentHour, 
    TO_CHAR (SYSDATE, 'MI') AS Roshan_CurrentMinutes,
    TO_CHAR (SYSDATE, 'SS') AS Roshan_CurrentSeconds 
FROM DUAL;
--5
SELECT
    Title AS Roshan_Book_Title,
    RPAD ('*', 12, '*') || TO_CHAR (Cost, '9990.99') AS Cost
FROM Books;
--6
SELECT
    Title AS RoshanBook_Title,
    PubDate AS Publication_Date,
    TRUNC(SYSDATE) AS Current_Date, 
    FLOOR(MONTHS_BETWEEN(TRUNC(SYSDATE), PubDate)) AS Age_In_Months
FROM Books;
--7
SELECT
  NEXT_DAY(SYSDATE, 'WEDNESDAY') AS Roshan_Next_Wednesday
FROM
  DUAL;
--8
SELECT
Customer# AS Roshan_Customer,
SUBSTR(Zip, 3, 1) AS Third_Digit_Zip, SUBSTR(Zip, 4, 1) AS Fourth_Digit_Zip, INSTR(TO_CHAR(Customer#), '3') AS Position_of_3
FROM Customers;

