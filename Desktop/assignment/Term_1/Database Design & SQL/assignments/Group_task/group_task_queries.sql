-- Customer Table
CREATE TABLE Customer (
    Driver_License_Number VARCHAR2(50 CHAR) PRIMARY KEY,
    First_Name VARCHAR2(50 CHAR) NOT NULL,
    Last_Name VARCHAR2(50 CHAR) NOT NULL,
    Street VARCHAR2(255 CHAR) NOT NULL,
    City VARCHAR2(50 CHAR) NOT NULL,
    Postal_Code VARCHAR2(10 CHAR) NOT NULL,
    Province VARCHAR2(50 CHAR) NOT NULL,
    Phone VARCHAR2(20 CHAR) NOT NULL,
    Email VARCHAR2(100 CHAR) NOT NULL,
    Member_ID VARCHAR2(50 CHAR),
    Gender VARCHAR2(10 CHAR)
);

-- Car Table
CREATE TABLE Car (
    Chassis_Number VARCHAR2(50 CHAR) PRIMARY KEY,
    Model VARCHAR2(50 CHAR) NOT NULL,
    Model_Number VARCHAR2(50 CHAR) NOT NULL,
    Is_Available CHAR(1 CHAR) NOT NULL CHECK (Is_Available IN ('Y', 'N')),
    Mileage NUMBER NOT NULL,
    No_Of_Person NUMBER NOT NULL,
    Price_Per_Day NUMBER(10, 2) NOT NULL,
    Late_Fee_Per_Hour NUMBER(10, 2) NOT NULL,
    No_Of_Luggage NUMBER NOT NULL,
    Insurance_Code VARCHAR2(50 CHAR) NOT NULL,
    Make VARCHAR2(50 CHAR),
    Condition VARCHAR2(50 CHAR)
);

-- Insurance Table
CREATE TABLE Insurance (
    Insurance_Code VARCHAR2(50 CHAR) PRIMARY KEY,
    Coverage_Type VARCHAR2(100 CHAR) NOT NULL,
    Cost_Per_Day NUMBER(10, 2) NOT NULL,
    Name VARCHAR2(100 CHAR)
);

-- Location Table
CREATE TABLE Location (
    Location_ID NUMBER PRIMARY KEY,
    Street VARCHAR2(255 CHAR) NOT NULL,
    City VARCHAR2(50 CHAR) NOT NULL,
    Postal_Code VARCHAR2(10 CHAR) NOT NULL,
    Province VARCHAR2(50 CHAR) NOT NULL
);

-- Office Table
CREATE TABLE Office (
    Office_ID NUMBER PRIMARY KEY,
    Name VARCHAR2(100 CHAR) NOT NULL,
    Address VARCHAR2(255 CHAR) NOT NULL,
    Postal_Code VARCHAR2(10 CHAR) NOT NULL,
    Province VARCHAR2(50 CHAR)
);

-- Employee Table
CREATE TABLE Employee (
    Employee_ID NUMBER PRIMARY KEY,
    First_Name VARCHAR2(50 CHAR) NOT NULL,
    Last_Name VARCHAR2(50 CHAR) NOT NULL,
    Address VARCHAR2(255 CHAR) NOT NULL,
    Office_ID NUMBER NOT NULL,
    Gender VARCHAR2(10 CHAR),
    Age NUMBER,
    FOREIGN KEY (Office_ID) REFERENCES Office(Office_ID)
);

-- Payment Table
CREATE TABLE Payment (
    Payment_ID NUMBER PRIMARY KEY,
    Payment_Type VARCHAR2(50 CHAR) NOT NULL,
    Payment_Due_Date DATE NOT NULL,
    Total_Amount NUMBER(10, 2) NOT NULL,
    Tax_Amount NUMBER(10, 2) NOT NULL,
    Payment_Status VARCHAR2(50 CHAR) NOT NULL,
    Driver_License_Number VARCHAR2(50 CHAR) NOT NULL,
    Contract_ID NUMBER NOT NULL,
    Advance_Amount NUMBER(10, 2),
    Cancelation_Charge NUMBER(10, 2),
    Late_Fee NUMBER(10, 2),
    FOREIGN KEY (Driver_License_Number) REFERENCES Customer(Driver_License_Number),
    FOREIGN KEY (Contract_ID) REFERENCES Contract(Contract_ID)
);

-- Contract Table
CREATE TABLE Contract (
    Contract_ID NUMBER PRIMARY KEY,
    Start_Date DATE NOT NULL,
    End_Date DATE NOT NULL,
    Contract_Status VARCHAR2(50 CHAR) NOT NULL,
    Return_Date DATE NOT NULL,
    Amount NUMBER(10, 2) NOT NULL,
    Chassis_Number VARCHAR2(50 CHAR) NOT NULL,
    Driver_License_Number VARCHAR2(50 CHAR) NOT NULL,
    Office_ID NUMBER NOT NULL,
    Location_ID NUMBER NOT NULL,
    FOREIGN KEY (Chassis_Number) REFERENCES Car(Chassis_Number),
    FOREIGN KEY (Driver_License_Number) REFERENCES Customer(Driver_License_Number),
    FOREIGN KEY (Office_ID) REFERENCES Office(Office_ID),
    FOREIGN KEY (Location_ID) REFERENCES Location(Location_ID)
);
