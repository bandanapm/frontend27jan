CREATE DATABASE GROUP_3
GO
USE GROUP_3
GO
CREATE TABLE Company(
	Company_Id INTEGER NOT NULL,
	Name VARCHAR(25) NOT NULL,
	Phone_Number INTEGER NOT NULL,
	Email VARCHAR(25) NOT NULL,
	Address VARCHAR(25) NOT NULL,
	CONSTRAINT Company_Company_Id_PK PRIMARY KEY(Company_Id),
	CONSTRAINT Company_Name_UK UNIQUE(Name),
	CONSTRAINT Company_Phone_Number_UK UNIQUE(Phone_Number),
	CONSTRAINT Company_Email_UK UNIQUE(Email)
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
	Warehouse_Id INTEGER NOT NULL,
	CONSTRAINT Employees_Hire_Date_DOB_CK CHECK(Hire_Date > DOB),
	CONSTRAINT Employees_Manager_Id_FK FOREIGN KEY(Manager_Id) REFERENCES Employees(Employee_ID),
	CONSTRAINT Employees_Mobile_Number_UK UNIQUE(Mobile_Number),
	CONSTRAINT Employees_Email_UK UNIQUE(Email),
	CONSTRAINT Employees_Gender_CK CHECK(Gender in ('M', 'F', 'O') )
)
GO
CREATE TABLE Warehouses(
	Warehouse_Id INTEGER NOT NULL,
	Company_Id INTEGER NOT NULL,
	Warehouse_Manager_Id INTEGER NULL,
	Phone_Number VARCHAR(10) NULL,
	Email VARCHAR(50) NOT NULL,
	Address VARCHAR(50) NOT NULL,
	CONSTRAINT Warehouses_Warehouse_Id_PK PRIMARY KEY(Warehouse_Id),
	CONSTRAINT Warehouses_Company_Id_FK FOREIGN KEY(Company_Id) REFERENCES Company(Company_Id),
	CONSTRAINT Warehouses_Warehouse_Manager_Id_FK FOREIGN KEY(Warehouse_Manager_Id) REFERENCES Employees(Employee_Id),
	CONSTRAINT Warehouses_Email_UK UNIQUE(Email)
)
GO
ALTER TABLE Employees
ADD CONSTRAINT Employees_Warehouse_Id_FK FOREIGN KEY(Warehouse_Id) REFERENCES Warehouses(Warehouse_Id)
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
	CONSTRAINT Inventory_Warehouse_Id_Fk FOREIGN KEY(Warehouse_Id) REFERENCES Warehouses(Warehouse_Id),
	CONSTRAINT Inventory_Product_Id_FK FOREIGN KEY(Product_Id) REFERENCES Products(Product_Id),
	CONSTRAINT Inventory_Shelves_Number_UK UNIQUE(Shelves_Number)
)
GO
CREATE TABLE Customers (
    Customer_Id INT PRIMARY KEY,
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
CREATE TABLE Order_Items(
	OrderItem_Id INTEGER PRIMARY KEY,
	Order_Id INTEGER NOT NULL,
	Product_Id INTEGER NOT NULL,
	Quantity DECIMAL(10, 2) NOT NULL,
	Discount DECIMAL(10, 2) NOT NULL,
	CONSTRAINT Order_Items_Product_Id_FK FOREIGN KEY(Product_Id) REFERENCES Products(Product_Id)
)
ALTER TABLE Order_Items
ADD CONSTRAINT Order_Items_Order_Id_FK FOREIGN KEY(Order_Id) REFERENCES Orders(Order_Id)
GO
INSERT INTO company VALUES
(1,'Oasis', 1234567890, 'oasis.hardware@gmail.com', '45 queen street west');

