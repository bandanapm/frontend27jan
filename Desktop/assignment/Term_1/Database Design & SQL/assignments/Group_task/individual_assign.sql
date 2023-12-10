-- 13. Find customers who haven't made any payments
SELECT * FROM Customer 
WHERE Driver_License_Number NOT IN (SELECT Driver_License_Number FROM Payment);

-- 14. List contracts and their respective payment statuses
SELECT Contract.Contract_ID, Payment.Payment_Status 
FROM Contract 
LEFT JOIN Payment ON Contract.Contract_ID = Payment.Contract_ID;

-- 15. Determine total amount paid for each car model
SELECT Car.Model, SUM(Payment.Total_Amount) AS Total_Paid 
FROM Payment 
JOIN Contract ON Payment.Contract_ID = Contract.Contract_ID 
JOIN Car ON Contract.Chassis_Number = Car.Chassis_Number 
GROUP BY Car.Model;

-- 16. Find all cars available in a specific city
SELECT Car.Model 
FROM Car 
JOIN Location ON Car.Chassis_Number = Location.Location_ID 
WHERE Location.City = 'New York' AND Car.Is_Available = 'Y';

-- 17. List all employees working in an office in a specific province
SELECT Employee.First_Name, Employee.Last_Name 
FROM Employee 
JOIN Office ON Employee.Office_ID = Office.Office_ID 
WHERE Office.Province = 'Ontario';

-- 18. Find all contracts that don't have a corresponding payment
SELECT Contract.Contract_ID 
FROM Contract 
WHERE Contract_ID NOT IN (SELECT Contract_ID FROM Payment);

-- 19. Get the total late fees collected from customers
SELECT SUM(Late_Fee) AS Total_Late_Fees FROM Payment;

-- 20. Find all customers who have rented a specific car model
SELECT Customer.First_Name, Customer.Last_Name 
FROM Customer 
JOIN Contract ON Customer.Driver_License_Number = Contract.Driver_License_Number 
JOIN Car ON Contract.Chassis_Number = Car.Chassis_Number 
WHERE Car.Model = 'Toyota Camry';

-- 21. Get the most popular car based on contracts
SELECT Car.Model, COUNT(Contract_ID) AS Number_Of_Contracts 
FROM Car 
JOIN Contract ON Car.Chassis_Number = Contract.Chassis_Number 
GROUP BY Car.Model 
ORDER BY Number_Of_Contracts DESC FETCH FIRST 1 ROW ONLY;

-- 22. List all cars insured with a specific insurance provider
SELECT Car.Model FROM Car WHERE Insurance_Code = 
(SELECT Insurance_Code FROM Insurance WHERE Name = 'XYZ Insurance');

-- 23. Determine the average contract amount for each car model
SELECT Car.Model, AVG(Contract.Amount) AS Avg_Amount 
FROM Car 
JOIN Contract ON Car.Chassis_Number = Contract.Chassis_Number 
GROUP BY Car.Model;

-- 24. Determine the total number of cars in each location
SELECT Location_ID, COUNT(*) AS Number_Of_Cars 
FROM Contract GROUP BY Location_ID;

-- 25. Get total revenue per office from car contracts
SELECT Office_ID, SUM(Amount) AS Total_Revenue 
FROM Contract GROUP BY Office_ID;

-- 26. List customers who have rented cars more than 5 times
SELECT Driver_License_Number, COUNT(*) AS Rentals 
FROM Contract 
GROUP BY Driver_License_Number 
HAVING COUNT(*) > 5;

-- 27. Get the total amount of all contracts where the return date has passed
SELECT SUM(Amount) AS Total_Revenue 
FROM Contract 
WHERE Return_Date < SYSDATE;

-- 28. List all cars with insurance coverage type "Full"
SELECT Model 
FROM Car 
WHERE Insurance_Code IN (SELECT Insurance_Code FROM Insurance WHERE Coverage_Type = 'Full');

-- 29. Get the average payment amount per customer
SELECT Driver_License_Number, AVG(Total_Amount) AS Avg_Payment 
FROM Payment GROUP BY Driver_License_Number;

-- 30. Determine the number of cars that are available vs. rented
SELECT Is_Available, COUNT(*) AS Number_Of_Cars 
FROM Car GROUP BY Is_Available;

-- 31. Determine the total number of contracts made in a specific year
SELECT COUNT(*) AS Contracts_In_2022 
FROM Contract 
WHERE EXTRACT(YEAR FROM Start_Date) = 2022;

-- 32. List the most recent contract for each customer
SELECT Driver_License_Number, MAX(Start_Date) AS Most_Recent_Contract 
FROM Contract 
GROUP BY Driver_License_Number;

-- 33. List employees who don't manage any office
SELECT * FROM Employee 
WHERE Employee_ID NOT IN (SELECT DISTINCT Office_ID FROM Office);

-- 34. Get all contracts that started and ended in different locations
SELECT Contract_ID 
FROM Contract 
WHERE Office_ID <> Location_ID;

-- 35. List offices that have generated more than $1000 in total contract amounts
SELECT Office_ID 
FROM Contract 
GROUP BY Office_ID 
HAVING SUM(Amount) > 1000;

-- 36. List all payments that have late fees greater than the advance amount
SELECT Payment_ID 
FROM Payment 
WHERE Late_Fee > Advance_Amount;

-- 37. List all insurance types that are used by more than 10 cars
SELECT Insurance_Code 
FROM Car 
GROUP BY Insurance_Code 
HAVING COUNT(*) > 10;

-- 38. List all cars that were rented in January 2023
SELECT Car.Model 
FROM Car 
JOIN Contract ON Car.Chassis_Number = Contract.Chassis_Number 
WHERE EXTRACT(MONTH FROM Contract.Start_Date) = 1 AND EXTRACT(YEAR FROM Contract.Start_Date) = 2023;

-- 39. Determine the office with the highest number of employees
SELECT Office_ID, COUNT(Employee_ID) AS Employee_Count 
FROM Employee 
GROUP BY Office_ID 
ORDER BY Employee_Count DESC FETCH FIRST 1 ROW ONLY;

-- 40. List all cars that have been rented but haven't been returned yet
SELECT Car.Model 
FROM Car 
JOIN Contract ON Car.Chassis_Number = Contract.Chassis_Number 
WHERE Contract.Return_Date IS NULL;

-- 41. Determine the oldest employee in each office
SELECT Office_ID, MAX(Age) AS Oldest_Age 
FROM Employee 
GROUP BY Office_ID;

-- 42. Get all payments that were due in the last 7 days
SELECT * 
FROM Payment 
WHERE Payment_Due_Date BETWEEN SYSDATE - 7 AND SYSDATE;

-- 43. List all contracts where the car make is "Toyota"
SELECT Contract_ID 
FROM Contract 
WHERE Chassis_Number IN (SELECT Chassis_Number FROM Car WHERE Make = 'Toyota');

-- 44. Determine the average cost per day of all insurances
SELECT AVG(Cost_Per_Day) AS Average_Insurance_Cost 
FROM Insurance;

-- 45. List the top 5 customers who have made the most number of contracts
SELECT Driver_License_Number, COUNT(*) AS Number_Of_Contracts 
FROM Contract 
GROUP BY Driver_License_Number 
ORDER BY Number_Of_Contracts DESC FETCH FIRST 5 ROWS ONLY;

-- 46. Determine the total revenue generated from contracts for each car make
SELECT Car.Make, SUM(Contract.Amount) AS Total_Revenue 
FROM Car 
JOIN Contract ON Car.Chassis_Number = Contract.Chassis_Number 
GROUP BY Car.Make;

-- 47. List all offices in the "Ontario" province with more than 3 employees
SELECT Office_ID 
FROM Employee 
WHERE Office_ID IN (SELECT Office_ID FROM Office WHERE Province = 'Ontario') 
GROUP BY Office_ID 
HAVING COUNT(Employee_ID) > 3;

-- 48. List all contracts with a late fee higher than the average late fee of all contracts
SELECT Contract_ID 
FROM Payment 
WHERE Late_Fee > (SELECT AVG(Late_Fee) FROM Payment);

-- 49. Get the youngest and oldest employee in the entire database
SELECT MIN(Age) AS Youngest, MAX(Age) AS Oldest FROM Employee;

-- 50. List the 3 most recent contracts
SELECT Contract_ID, Start_Date 
FROM Contract 
ORDER BY Start_Date DESC FETCH FIRST 3 ROWS ONLY;
