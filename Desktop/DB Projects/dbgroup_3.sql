CREATE DATABASE GROUP_3
GO
USE GROUP_3
GO
CREATE TABLE Company(
	Company_Id INTEGER NOT NULL,
	Name VARCHAR(25) NOT NULL,
	Phone_Number INTEGER NOT NULL,
	Email VARCHAR(25) NOT NULL,
	Address VARCHAR(25) NOT NULL
)
GO
CREATE TABLE Employees(
	Employee_Id INTEGER PRIMARY KEY,
	First_Name VARCHAR(10) NOT NULL,
	Middle_Name CHARACTER(1) NULL,
	Last_Name VARCHAR(10) NOT NULL,
	DOB DATE NOT NULL,
	Gender VARCHAR(8) NOT NULL,
	Mobile_Number VARCHAR(10) NOT NULL,
	Email VARCHAR(50) NOT NULL,
	Hire_Date DATE NOT NULL DEFAULT GETDATE(),
	Address VARCHAR(50) NOT NULL,
	Manager_Id INTEGER NULL,
	Warehouse_Id INTEGER NOT NULL
)
GO
CREATE TABLE Warehouses(
	Warehouse_Id INTEGER NOT NULL,
	Company_Id INTEGER NOT NULL,
	Warehouse_Manager_Id INTEGER NULL,
	Phone_Number VARCHAR(10) NULL,
	Email VARCHAR(50) NOT NULL,
	Address VARCHAR(50) NOT NULL
)
GO
CREATE TABLE Category(
	Category_Id INTEGER PRIMARY KEY,
	Name Varchar(50) NOT NULL,
	CONSTRAINT Category_Name_UK UNIQUE(Name)
)
GO
CREATE TABLE Products(
	Product_Id INTEGER PRIMARY KEY,	
	Name VARCHAR(20) NOT NULL,
	Category_Id INTEGER NOT NULL, 
	Serial_number CHARACTER	(15) NOT NULL,
	Description	VARCHAR	(100) NULL,
	Size INTEGER NULL,
	Color VARCHAR(20) NULL,
	Weight DECIMAL(5,2) NULL,
	Height DECIMAL(3,2) NULL,
	Length DECIMAL(3,2) NULL,
	Width DECIMAL(3,2) NULL,
	Price DECIMAL(10,2) NULL,
	Ratings DECIMAL(2,1) NULL,
	CONSTRAINT Products_Category_Id_Fk FOREIGN KEY(Category_Id) REFERENCES Category(Category_Id),
	CONSTRAINT Products_Serial_Number_UK UNIQUE(Serial_number)
)
GO
CREATE TABLE Inventory(
	Inventory_Id  INTEGER  PRIMARY KEY,
	Warehouse_Id INTEGER  NOT NULL,
	Product_Id  INTEGER  NOT NULL,
	Shelves_Number  INTEGER  NOT NULL UNIQUE,
	Quantity DECIMAL(10,2) NOT NULL,
	CONSTRAINT Inventory_Product_Id_FK FOREIGN KEY(Product_Id) REFERENCES Products(Product_Id),
	CONSTRAINT Inventory_Shelves_Number_UK UNIQUE(Shelves_Number)
)
GO
CREATE TABLE Customers (
    Customer_Id INT PRIMARY KEY IDENTITY(1,1),
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    DOB DATE NULL,
    Gender CHARACTER(1) NULL,
    Mobile_Number VARCHAR(10) NOT NULL UNIQUE,
    Email VARCHAR(50) NOT NULL UNIQUE,
    Username VARCHAR(10) NOT NULL UNIQUE,
    Password VARCHAR(12) NOT NULL,
    Billing_Address VARCHAR(255),
	CONSTRAINT Customers_Gender_CK CHECK(Gender in ('M', 'F', 'O') )
)
GO
CREATE TABLE Orders (
    Order_Id INT PRIMARY KEY,
    Customer_Id INT NOT NULL,
    Order_Date DATE NOT NULL,
    Order_Status VARCHAR(8) NULL DEFAULT 'Pending',
    Shipping_Address VARCHAR(50) NOT NULL,	
    Payment_Method VARCHAR(8) NOT NULL,
    Shipping_Cost DECIMAL(10, 2) NOT NULL,
    Shipping_Method VARCHAR(8) NOT NULL,
    Delivery_Date DATE NOT NULL,
    Tracking_Number VARCHAR(10) NOT NULL UNIQUE,
    Order_Notes VARCHAR(50),
    CONSTRAINT Order_Customer_Id_FK FOREIGN KEY (Customer_Id) REFERENCES Customers(Customer_Id),
	CONSTRAINT Order_Order_Status_CK CHECK(Order_Status in ('Pending', 'Processing', 'Completed') )
)
GO
CREATE SEQUENCE Orders_Seq
  START WITH 1
  INCREMENT BY 1;
GO
CREATE TABLE Order_Items(
	OrderItem_Id INTEGER PRIMARY KEY,
	Order_Id INTEGER NOT NULL,
	Product_Id INTEGER NOT NULL,
	Quantity DECIMAL(10, 2) NOT NULL,
	Discount DECIMAL(10, 2) NOT NULL,
	CONSTRAINT Order_Items_Product_Id_FK FOREIGN KEY(Product_Id) REFERENCES Products(Product_Id)
)
GO
ALTER TABLE Company
ADD CONSTRAINT Company_Company_Id_PK PRIMARY KEY(Company_Id)

ALTER TABLE Company
ADD CONSTRAINT Company_Name_UK UNIQUE(Name)

ALTER TABLE Company
ADD CONSTRAINT Company_Phone_Number_UK UNIQUE(Phone_Number)

ALTER TABLE Company
ADD CONSTRAINT Company_Email_UK UNIQUE(Email)

ALTER TABLE Warehouses
ADD CONSTRAINT Warehouses_Warehouse_Id_PK PRIMARY KEY(Warehouse_Id)

ALTER TABLE Warehouses
ADD CONSTRAINT Warehouses_Company_Id_FK FOREIGN KEY(Company_Id) REFERENCES Company(Company_Id)

ALTER TABLE Warehouses
ADD CONSTRAINT Warehouses_Warehouse_Manager_Id_FK FOREIGN KEY(Warehouse_Manager_Id) REFERENCES Employees(Employee_Id)

ALTER TABLE Warehouses
ADD CONSTRAINT Warehouses_Email_UK UNIQUE(Email)

ALTER TABLE Employees
ADD CONSTRAINT Employees_Warehouse_Id_FK FOREIGN KEY(Warehouse_Id) REFERENCES Warehouses(Warehouse_Id)

ALTER TABLE Employees
ADD CONSTRAINT Employees_Hire_Date_DOB_CK CHECK(Hire_Date > DOB)

ALTER TABLE Employees
ADD CONSTRAINT Employees_Manager_Id_FK FOREIGN KEY(Manager_Id) REFERENCES Employees(Employee_ID)

ALTER TABLE Employees
ADD CONSTRAINT Employees_Mobile_Number_UK UNIQUE(Mobile_Number)

ALTER TABLE Employees
ADD CONSTRAINT Employees_Email_UK UNIQUE(Email)

ALTER TABLE Employees
ADD CONSTRAINT Employees_Gender_CK CHECK(Gender in ('M', 'F', 'O') )

ALTER TABLE Inventory
ADD CONSTRAINT Inventory_Warehouse_Id_Fk FOREIGN KEY(Warehouse_Id) REFERENCES Warehouses(Warehouse_Id)

ALTER TABLE Order_Items
ADD CONSTRAINT Order_Items_Order_Id_FK FOREIGN KEY(Order_Id) REFERENCES Orders(Order_Id)



-- DATA TO INSERT

GO
INSERT Category (Category_Id, Name) 
VALUES (1, 'Paint')
GO
INSERT Company (Company_Id, Name, Phone_Number, Email, Address) 
VALUES (1, 'Oasis', 1234567890, 'oasis.hardware@gmail.com', '45 queen street west')
GO
INSERT Warehouses (Warehouse_Id, Company_Id, Warehouse_Manager_Id, Phone_Number, Email, Address) 
VALUES (11, 1, NULL, NULL, '8527419632', 'warehouse@mail.com')
GO
INSERT Products (Product_Id, Name, Category_Id, Serial_number, Description, Size, Color, Weight, Height, Length, Width, Price, Ratings) 
VALUES (1, 'Red Oil Paint Color', 1, '7847JK90PA023  ', 'Paint used for artistics oil paints.', NULL, 'Red', 5.00, NULL, NULL, NULL, 180.00, 4.3),
		(2, 'White Oil Paint', 1, '7347GR90PA023  ', 'Paint used for artistics oil paints.', NULL, 'White', 5.00, NULL, NULL, NULL, 180.00, 4.3 ),
		(3, 'Green Oil Paint', 1, '7347PO90PA023  ', 'Paint used for artistics oil paints.', NULL, 'Gree', 5.00, NULL, NULL, NULL, 180.00, 4.3 )
GO
INSERT Customers (First_Name, Last_Name, DOB, Gender, Mobile_Number, Email, Username, Password, Billing_Address) 
VALUES ('Hari', 'Dai', '1990-01-01', 'M', '1234567890', 'hari.dai@example.com', 'hari_dai', 'password123', '123 Victoria Park')
GO
INSERT Employees (Employee_Id, First_Name, Middle_Name, Last_Name, DOB, Gender, Mobile_Number, Email, Hire_Date, Address, Manager_Id, Warehouse_Id) 
VALUES (1001, 'Joe', 'K', 'Philip', '1996-01-08', 'M', '6478958541', 'joe@gmail.com', '2022-08-15', '2011 Interiors Blvd', NULL, 11),
		(1002, 'Morriso', NULL, 'Toni', '1994-02-18', 'F', '6473145868', 'toni@gmail.com', '2020-01-10', 'Rua Frei Caneca 1360', 1001, 11),
		(1003, 'Solotaroff', NULL, 'Paul', '1993-06-28', 'F', '4233167351', 'Paul@gmail.com', '2020-01-10', 'Mariano Escobedo 9991', 1002, 11),
		(1004, 'Ambrose', NULL, 'Stephen E.', '1994-09-12', 'M', '1235148302', 'ambrose@gmail.com', '2023-11-26', 'Mariano Escobedo 91', 1002, 11),
		(1005, 'Joh', NULL, 'Kip', '1998-02-21', 'M', '7894561230', 'john@mail.com', '2023-11-26', 'Victoriya Park 14578', NULL, 11)
GO
INSERT INTO Employees (Employee_Id, First_Name, Middle_Name, Last_Name, DOB, Gender, Mobile_Number, Email, Address, Manager_Id, Warehouse_Id)
VALUES(1006, 'Roger', NULL, 'KD', '1991-12-21', 'M', '7894568430', 'kd@mail.com', 'Victoriya Park 178', NULL, 11)
GO
INSERT Inventory (Inventory_Id, Warehouse_Id, Product_Id, Shelves_Number, Quantity) 
VALUES (1, 11, 1, 2, 10.02)
GO
INSERT Orders (Order_Id, Customer_Id, Order_Date, Order_Status, Shipping_Address, Payment_Method, Shipping_Cost, Shipping_Method, Delivery_Date, Tracking_Number, Order_Notes) 
VALUES (NEXT VALUE FOR Orders_Seq, 1, '2023-11-18', 'Pending', '123 Main Street, Cityville', 'Credit', 10.00, 'Standard', '2023-11-25', 'ABC123456', 'Some order notes')
GO
INSERT Order_Items (OrderItem_Id, Order_Id, Product_Id, Quantity, Discount) 
VALUES (1, 1, 1, 5.00, 0.00)
GO
