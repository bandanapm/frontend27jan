-- CREATE --
CREATE TABLE Customer_142 (
    Driver_License_Number VARCHAR2(20) PRIMARY KEY,
    First_Name VARCHAR2(100) NOT NULL,
    Last_Name VARCHAR2(100) NOT NULL,
    Street VARCHAR2(255) NOT NULL,
    City VARCHAR2(50) NOT NULL,
    Postal_Code VARCHAR2(10) NOT NULL,
    Province VARCHAR2(50) NOT NULL,
    Phone VARCHAR2(15) NOT NULL,
    Email VARCHAR2(150) NOT NULL,
    Member_ID VARCHAR2(20),
    Gender CHAR(1)
);

CREATE TABLE Car_142 (
    Chassis_Number VARCHAR2(25) PRIMARY KEY,
    Model VARCHAR2(100) NOT NULL,
    Model_Number VARCHAR2(50) NOT NULL,
    Is_Available CHAR(1) NOT NULL,
    Mileage NUMBER(10,2) NOT NULL,
    No_Of_Person INT NOT NULL,
    Price_Per_Day NUMBER(10,2) NOT NULL,
    Late_Fee_Per_Hour NUMBER(10,2) NOT NULL,
    No_Of_Luggage INT NOT NULL,
    Insurance_Code VARCHAR2(20) NOT NULL,
    Make VARCHAR2(100),
    Condition VARCHAR2(50)
);

CREATE TABLE Insurance_142 (
    Insurance_Code VARCHAR2(20) PRIMARY KEY,
    Coverage_Type VARCHAR2(100) NOT NULL,
    Cost_Per_Day NUMBER(10,2) NOT NULL,
    Name VARCHAR2(150)
);

CREATE TABLE Location_142 (
    Location_ID INT PRIMARY KEY,
    Street VARCHAR2(255) NOT NULL,
    City VARCHAR2(50) NOT NULL,
    Postal_Code VARCHAR2(10) NOT NULL,
    Province VARCHAR2(50) NOT NULL
);

CREATE TABLE Office_142 (
    Office_ID INT PRIMARY KEY,
    Name VARCHAR2(100) NOT NULL,
    Address VARCHAR2(255) NOT NULL,
    Postal_Code VARCHAR2(10) NOT NULL,
    Province VARCHAR2(50)
);

CREATE TABLE Employee_142 (
    Employee_ID INT PRIMARY KEY,
    First_Name VARCHAR2(100) NOT NULL,
    Last_Name VARCHAR2(100) NOT NULL,
    Address VARCHAR2(255) NOT NULL,
    Office_ID INT NOT NULL,
    Gender CHAR(1),
    Age INT
);

CREATE TABLE Payment_142 (
    Payment_ID INT PRIMARY KEY,
    Payment_Type VARCHAR2(50) NOT NULL,
    Payment_Due_Date DATE NOT NULL,
    Total_Amount NUMBER(10,2) NOT NULL,
    Tax_Amount NUMBER(10,2) NOT NULL,
    Payment_Status VARCHAR2(50) NOT NULL,
    Driver_License_Number VARCHAR2(20) NOT NULL,
    Contract_ID INT NOT NULL,
    Advance_Amount NUMBER(10,2),
    Cancelation_Charge NUMBER(10,2),
    Late_Fee NUMBER(10,2)
);

CREATE TABLE Contract_142 (
    Contract_ID INT PRIMARY KEY,
    Start_Date DATE NOT NULL,
    End_Date DATE NOT NULL,
    Contract_Status VARCHAR2(50) NOT NULL,
    Return_Date DATE NOT NULL,
    Amount NUMBER(10,2) NOT NULL,
    Chassis_Number VARCHAR2(25) NOT NULL,
    Driver_License_Number VARCHAR2(20) NOT NULL,
    Office_ID INT NOT NULL,
    Location_ID INT NOT NULL
);

-- INSERT --
-- Inserting into Customer_142 table
INSERT INTO Customer_142 (Driver_License_Number, First_Name, Last_Name, Street, City, Postal_Code, Province, Phone, Email, Member_ID, Gender)
VALUES ('DL12345', 'John', 'Doe', '123 Main St', 'New York', '10001', 'NY', '1234567890', 'john.doe@email.com', 'M123', 'M');

INSERT INTO Customer_142 (Driver_License_Number, First_Name, Last_Name, Street, City, Postal_Code, Province, Phone, Email, Member_ID, Gender)
VALUES ('DL4488', 'Roshan', 'Shrestha', '88 Main St', 'New Jersey', '20099', 'BC', '123457890', 'roshan@email.com', NULL, 'M');

INSERT INTO Customer_142 (Driver_License_Number, First_Name, Last_Name, Street, City, Postal_Code, Province, Phone, Email, Member_ID, Gender)
VALUES ('D88', 'Albert', 'Adison', '8 Main St', 'New Buffalo', '2099', 'VC', '1257890', 'albert@email.com', NULL, 'M');

INSERT INTO Customer_142 (Driver_License_Number, First_Name, Last_Name, Street, City, Postal_Code, Province, Phone, Email, Member_ID, Gender)
VALUES ('DL67890', 'Alice', 'Brown', '456 Elm St', 'Boston', '02134', 'MA', '0987654321', 'alice.brown@email.com', NULL, 'F');

INSERT INTO Customer_142 (Driver_License_Number, First_Name, Last_Name, Street, City, Postal_Code, Province, Phone, Email, Member_ID, Gender)
VALUES ('DL009', 'Roshan', 'Shrestha', '242 Alvert St', 'New Jersyy', '2009', 'ON', '88672888', 'roshan@email.com', 'MM8', 'M');

-- Inserting into Car_142 table
INSERT INTO Car_142 
(Chassis_Number, Model, Model_Number, Is_Available, Mileage, No_Of_Person, Price_Per_Day, Late_Fee_Per_Hour, No_Of_Luggage, Insurance_Code, Make, Condition)
VALUES ('CH12345', 'Sedan', 'S123', 'Y', 50000, 5, 100, 10, 4, 'IC123', 'Toyota', 'New');

INSERT INTO Car_142 
(Chassis_Number, Model, Model_Number, Is_Available, Mileage, No_Of_Person, Price_Per_Day, Late_Fee_Per_Hour, No_Of_Luggage, Insurance_Code, Make, Condition)
VALUES ('CH12459', 'Maybach', 'M123', 'Y', 20000, 3, 300, 40, 8, 'IC12', 'Mercedes', 'New');

INSERT INTO Car_142 
(Chassis_Number, Model, Model_Number, Is_Available, Mileage, No_Of_Person, Price_Per_Day, Late_Fee_Per_Hour, No_Of_Luggage, Insurance_Code, Make, Condition)
VALUES ('CH12005', 'MMY', 'D123', 'Y', 9000.50, 1, 49.50, 120.00, 6, 'INS001', 'Mercedes', 'BRAND');

-- Inserting into Insurance_142 table
INSERT INTO Insurance_142 (Insurance_Code, Coverage_Type, Cost_Per_Day, Name)
VALUES ('IC123', 'Full', 15, 'Best Insurance');

INSERT INTO Insurance_142 (Insurance_Code, Coverage_Type, Cost_Per_Day, Name)
VALUES ('IC456', 'Partial', 10.5, 'Standard Insurance');

INSERT INTO Insurance_142 (Insurance_Code, Coverage_Type, Cost_Per_Day, Name)
VALUES ('IC678', 'Third Party', 7.25, 'Basic Insurance');

-- Inserting into Location_142 table
INSERT INTO Location_142 (Location_ID, Street, City, Postal_Code, Province)
VALUES (1, '456 Market St', 'Los Angeles', '90001', 'CA');

INSERT INTO Location_142 (Location_ID, Street, City, Postal_Code, Province)
VALUES (2, '789 Oak St', 'San Francisco', '94110', 'CA');

INSERT INTO Location_142 (Location_ID, Street, City, Postal_Code, Province)
VALUES (3, '321 Maple St', 'Chicago', '60601', 'IL');

-- Inserting into Office_142 table
INSERT INTO Office_142 (Office_ID, Name, Address, Postal_Code, Province)
VALUES (1, 'Main Office', '789 Central St', '20001', 'DC');

INSERT INTO Office_142 (Office_ID, Name, Address, Postal_Code, Province)
VALUES (2, 'Downtown Office', '123 Pine St', '90210', 'CA');

INSERT INTO Office_142 (Office_ID, Name, Address, Postal_Code, Province)
VALUES (3, 'Uptown Office', '555 Oak St', '90220', 'IL');

-- Inserting into Employee_142 table
INSERT INTO Employee_142 (Employee_ID, First_Name, Last_Name, Address, Office_ID, Gender, Age)
VALUES (1, 'Jane', 'Smith', '101 Central St', 1, 'F', 30);

INSERT INTO Employee_142 (Employee_ID, First_Name, Last_Name, Address, Office_ID, Gender, Age)
VALUES (2, 'Michael', 'Johnson', '222 Pine St', 2, 'M', 28);

INSERT INTO Employee_142 (Employee_ID, First_Name, Last_Name, Address, Office_ID, Gender, Age)
VALUES (3, 'David', 'Miller', '333 Oak St', 3, 'M', 35);

-- Inserting into Payment_142 table
INSERT INTO Payment_142 (Payment_ID, Payment_Type, Payment_Due_Date, Total_Amount, Tax_Amount, Payment_Status, Driver_License_Number, Contract_ID, Advance_Amount, Cancelation_Charge, Late_Fee)
VALUES (1, 'Credit Card', TO_DATE('2023-08-10', 'YYYY-MM-DD'), 500, 50, 'Pending', 'DL12345', 1, 100, 20, 10);

INSERT INTO Payment_142 (Payment_ID, Payment_Type, Payment_Due_Date, Total_Amount, Tax_Amount, Payment_Status, Driver_License_Number, Contract_ID, Advance_Amount, Cancelation_Charge, Late_Fee)
VALUES (2, 'Cash', TO_DATE('2023-08-15', 'YYYY-MM-DD'), 350, 35, 'Paid', 'DL4488', 2, NULL, NULL, NULL);

INSERT INTO Payment_142 (Payment_ID, Payment_Type, Payment_Due_Date, Total_Amount, Tax_Amount, Payment_Status, Driver_License_Number, Contract_ID, Advance_Amount, Cancelation_Charge, Late_Fee)
VALUES (3, 'Debit Card', TO_DATE('2023-08-20', 'YYYY-MM-DD'), 200, 20, 'Paid', 'DL12345', 3, 50, 10, 5);

-- Inserting into Contract_142 table
INSERT INTO Contract_142 (Contract_ID, Start_Date, End_Date, Contract_Status, Return_Date, Amount, Chassis_Number, Driver_License_Number, Office_ID, Location_ID)
VALUES (1, TO_DATE('2023-08-01', 'YYYY-MM-DD'), TO_DATE('2023-08-10', 'YYYY-MM-DD'), 'Active', TO_DATE('2023-08-10', 'YYYY-MM-DD'), 450, 'CH12345', 'DL12345', 1, 1);

INSERT INTO Contract_142 (Contract_ID, Start_Date, End_Date, Contract_Status, Return_Date, Amount, Chassis_Number, Driver_License_Number, Office_ID, Location_ID)
VALUES (2, TO_DATE('2023-08-05', 'YYYY-MM-DD'), TO_DATE('2023-08-12', 'YYYY-MM-DD'), 'Active', TO_DATE('2023-08-12', 'YYYY-MM-DD'), 300, 'CH12459', 'DL4488', 2, 2);

INSERT INTO Contract_142 (Contract_ID, Start_Date, End_Date, Contract_Status, Return_Date, Amount, Chassis_Number, Driver_License_Number, Office_ID, Location_ID)
VALUES (3, TO_DATE('2023-08-08', 'YYYY-MM-DD'), TO_DATE('2023-08-15', 'YYYY-MM-DD'), 'Active', TO_DATE('2023-08-15', 'YYYY-MM-DD'), 150, 'CH12005', 'DL67890', 3, 3);

INSERT INTO Contract_142 (Contract_ID, Start_Date, End_Date, Contract_Status, Return_Date, Amount, Chassis_Number, Driver_License_Number, Office_ID, Location_ID)
VALUES (1001, TO_DATE('2023-08-20', 'YYYY-MM-DD'), TO_DATE('2028-08-10', 'YYYY-MM-DD'), 'Active', TO_DATE('2024-08-10', 'YYYY-MM-DD'), 450, 'CH45', 'DL9899', 4, 2);





-- CATEGORY A --
SELECT First_Name, Last_Name, Email FROM Customer_142;

SELECT Model, Price_Per_Day * 7 AS Weekly_Price FROM Car_142;

SELECT First_Name, Member_ID FROM Customer_142 WHERE Member_ID IS NULL;

SELECT First_Name, Member_ID FROM Customer_142 WHERE Member_ID IS NOT NULL;

SELECT First_Name || ' ' || Last_Name AS Full_Name FROM Customer_142;

SELECT DISTINCT City FROM Customer_142;

SELECT Model FROM Car_142 WHERE NOT Model = 'Sedan';

-- CATEGORY B --
SELECT First_Name, Last_Name FROM Customer_142 WHERE Postal_Code BETWEEN '10000' AND '20000';

SELECT Model FROM Car_142 WHERE Make IN ('Toyota', 'Honda');

SELECT Model FROM Car_142 WHERE Make NOT IN ('Toyota', 'Honda');

SELECT First_Name FROM Customer_142 WHERE First_Name LIKE 'J%';

SELECT Model, Mileage FROM Car_142 WHERE Mileage > 30000 AND Price_Per_Day <= 100;

SELECT First_Name, Last_Name FROM Customer_142 WHERE Gender = 'M';

SELECT First_Name, Last_Name FROM Customer_142 WHERE Last_Name LIKE 'A%' AND First_Name  IN ('Alice', 'Albert');


-- CATEGORY C --
SELECT First_Name, Last_Name FROM Customer_142 WHERE City = 'New York' AND NOT Gender = 'F';

SELECT Model FROM Car_142 WHERE (Make = 'Toyota' OR Make = 'Honda') AND Mileage > 30000;

SELECT First_Name, Last_Name FROM Customer_142 ORDER BY Last_Name ASC;

SELECT AVG(Price_Per_Day) AS Avg_Price FROM Car_142 WHERE Make = 'Toyota';

SELECT COUNT(DISTINCT Make) as Unique_Makes, SUM(Price_Per_Day) as Total_Daily_Price, AVG(Mileage) as Average_Mileage FROM Car_142;

-- CATEGORY D
SELECT Province, COUNT(*) AS Customer_Count
FROM Customer_142
GROUP BY Province;

SELECT Office_ID, AVG(Age) AS Avg_Age
FROM Employee_142
GROUP BY Office_ID
HAVING AVG(Age) > 30;

SELECT TO_CHAR(Start_Date, 'DD-MON-YYYY') AS Formatted_Start_Date
FROM Contract_142
WHERE ROWNUM = 1;

SELECT LOWER(First_Name) AS Lowercase_Name
FROM Customer_142
WHERE ROWNUM = 1;

SELECT UPPER(Last_Name) AS Uppercase_Last_Name
FROM Customer_142
WHERE ROWNUM = 1;

SELECT INITCAP(Street) AS Proper_Street
FROM Customer_142
WHERE ROWNUM = 1;

SELECT CONCAT(First_Name, CONCAT(' ', Last_Name)) AS Full_Name
FROM Customer_142
WHERE ROWNUM = 1;

SELECT SUBSTR(Phone, 1, 3) AS Area_Code
FROM Customer_142
WHERE ROWNUM = 1;

SELECT INSTR(Email, '@') AS At_Symbol_Position
FROM Customer_142
WHERE ROWNUM = 1;

SELECT TRIM('A' FROM 'AABBBAA') AS Trimmed_String
FROM Customer_142
WHERE ROWNUM = 1;

SELECT RPAD(First_Name, 10, '*') AS Padded_Name
FROM Customer_142
WHERE ROWNUM = 1;

SELECT ROUND(Price_Per_Day, 1) AS Rounded_Price
FROM Car_142
WHERE ROWNUM = 1;

SELECT CEIL(Mileage) AS Rounded_Mileage
FROM Car_142
WHERE ROWNUM = 1;

SELECT NVL(Member_ID, 'No Member') AS Membership_Status
FROM Customer_142
WHERE ROWNUM = 1;

-- CATEGORY E --
SELECT c.First_Name, c.Last_Name, car.Model
FROM Customer_142 c
JOIN Contract_142 con ON c.Driver_License_Number = con.Driver_License_Number
JOIN Car_142 car ON con.Chassis_Number = car.Chassis_Number
WHERE ROWNUM = 1;

SELECT c.First_Name, c.Last_Name, con.Contract_ID
FROM Customer_142 c
LEFT JOIN Contract_142 con ON c.Driver_License_Number = con.Driver_License_Number
WHERE ROWNUM = 1;

SELECT c.First_Name, con.Contract_ID, con.Start_Date
FROM Customer_142 c
RIGHT JOIN Contract_142 con ON c.Driver_License_Number = con.Driver_License_Number
WHERE ROWNUM = 1;

SELECT c.First_Name, o.Name
FROM Customer_142 c
CROSS JOIN Office_142 o
WHERE ROWNUM = 1;

SELECT e1.First_Name AS Employee1, e2.First_Name AS Employee2
FROM Employee_142 e1
JOIN Employee_142 e2 ON e1.Office_ID = e2.Office_ID
WHERE ROWNUM <= 1;

-- CATEGORY F --
SELECT Chassis_Number, Model, Price_Per_Day
FROM Car_142
WHERE Price_Per_Day < (SELECT AVG(Price_Per_Day) FROM Car_142);

SELECT c.First_Name, c.Last_Name
FROM Customer_142 c
WHERE EXISTS (SELECT 1 FROM Contract_142 con WHERE con.Driver_License_Number = c.Driver_License_Number);

SELECT c.First_Name, c.Last_Name
FROM Customer_142 c
WHERE NOT EXISTS (SELECT 1 FROM Contract_142 con WHERE con.Driver_License_Number = c.Driver_License_Number);

SELECT First_Name, Last_Name FROM Customer_142
UNION
SELECT First_Name, Last_Name FROM Employee_142;

SELECT First_Name
FROM Customer_142
WHERE Gender = 'M'
INTERSECT
SELECT First_Name
FROM Customer_142
WHERE Last_Name LIKE '%son%';

SELECT First_Name
FROM Customer_142
WHERE Gender = 'M'
MINUS
SELECT First_Name
FROM Customer_142
WHERE Last_Name LIKE '%son%';

-- ADVANCE SQL --
SELECT Car.Model
FROM Car_142 Car
WHERE Car.Chassis_Number IN (
    SELECT Chassis_Number
    FROM Contract_142
    GROUP BY Chassis_Number
    HAVING COUNT(*) = (
        SELECT MAX(Rentals)
        FROM (
            SELECT Chassis_Number, COUNT(*) AS Rentals
            FROM Contract_142
            GROUP BY Chassis_Number
        )
    )
);

SELECT C.First_Name, C.Last_Name, P.Total_Amount
FROM Customer_142 C
JOIN Payment_142 P ON C.Driver_License_Number = P.Driver_License_Number
WHERE P.Total_Amount >= ALL (
    SELECT MAX(Total_Amount)
    FROM Payment_142
    GROUP BY Driver_License_Number
);

SELECT C.First_Name, C.Last_Name
FROM Customer_142 C
WHERE NOT EXISTS (
    SELECT 1
    FROM Contract_142 CO
    WHERE CO.Driver_License_Number = C.Driver_License_Number
);

SELECT CO.Contract_ID, CO.Start_Date, I.Coverage_Type
FROM Contract_142 CO
JOIN Car_142 Car ON CO.Chassis_Number = Car.Chassis_Number
JOIN Insurance_142 I ON Car.Insurance_Code = I.Insurance_Code
WHERE CO.Chassis_Number IS NOT NULL;

SELECT E.First_Name
FROM Employee_142 E
WHERE E.Employee_ID IN (
    SELECT Office_ID
    FROM (
        SELECT Office_ID, COUNT(*) AS Office_Count
        FROM Location_142
        GROUP BY Office_ID
        ORDER BY Office_Count DESC
    )
    WHERE ROWNUM <= 1
);

SELECT First_Name, Last_Name
FROM Customer_142
WHERE Driver_License_Number IN (
    SELECT Driver_License_Number
    FROM Contract_142
    WHERE Chassis_Number IN (
        SELECT Chassis_Number
        FROM Car_142
        WHERE Mileage = (
            SELECT MAX(Mileage)
            FROM Car_142
        )
    )
);
