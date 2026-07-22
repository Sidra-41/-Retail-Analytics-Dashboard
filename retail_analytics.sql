CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    CostPrice DECIMAL(10,2),
    SellingPrice DECIMAL(10,2),
    PRIMARY KEY (ProductID)
);
CREATE TABLE Stores (
    StoreID INT AUTO_INCREMENT,
    StoreName VARCHAR(100),
    City VARCHAR(50),
    Region VARCHAR(50),
    PRIMARY KEY (StoreID)
);
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    Gender VARCHAR(10),
    AgeGroup VARCHAR(20),
    PRIMARY KEY (CustomerID)
);
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT,
    SaleDateTime DATETIME NOT NULL,
    ProductID INT,
    StoreID INT,
    CustomerID INT,
    Quantity INT,
    PaymentMethod VARCHAR(20),

    PRIMARY KEY (SaleID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (StoreID) REFERENCES Stores(StoreID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    StoreID INT,
    ProductID INT,
    StockAvailable INT,

    PRIMARY KEY (InventoryID),
    FOREIGN KEY (StoreID) REFERENCES Stores(StoreID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
SHOW TABLES;
SELECT * FROM Stores;
SELECT * FROM Customers;
SELECT * FROM Sales;
SELECT COUNT(*) FROM Sales;
SELECT * FROM Inventory ;
SELECT * FROM Inventory;

-- ALTER TABLE Sales
-- ADD COLUMN UnitCost DECIMAL(10,2),
-- ADD COLUMN SalesChannel VARCHAR(20);

-- ALTER TABLE Sales AUTO_INCREMENT = 1;
-- DELETE FROM Sales where SaleID > 0 ;
DESCRIBE Sales;

ALTER TABLE Sales
MODIFY ProductID INT NOT NULL,
MODIFY StoreID INT NOT NULL,
MODIFY CustomerID INT NOT NULL,
MODIFY Quantity INT NOT NULL,
MODIFY PaymentMethod VARCHAR(20) NOT NULL,
MODIFY UnitPrice DECIMAL(10,2) NOT NULL,
MODIFY UnitCost DECIMAL(10,2) NOT NULL,
MODIFY Discount DECIMAL(5,2) NOT NULL DEFAULT 0,
MODIFY TotalAmount DECIMAL(10,2) NOT NULL,
MODIFY SalesChannel VARCHAR(20) NOT NULL;

SELECT ProductID,
       ProductName,
       CostPrice,
       SellingPrice
FROM Products;

SELECT ProductID, CostPrice, SellingPrice
FROM Products;

SELECT *
FROM Inventory
WHERE StoreID = 3
AND ProductID = 8;

SELECT 
    SUM(Quantity) AS TotalSold
FROM Sales
WHERE ProductID = 8
AND StoreID = 3;

SELECT 
    COUNT(*) 
FROM Inventory
WHERE StockAvailable < 0;

SELECT * 
FROM Sales
ORDER BY SaleID DESC
LIMIT 10;

SELECT 
    SUM(TotalAmount) AS Total_Revenue
FROM Sales;

SELECT 
    SUM((UnitPrice - UnitCost) * Quantity) AS Total_Profit
FROM Sales;

SELECT 
    SUM(TotalAmount) AS Total_Revenue
FROM Sales;

SELECT
    SUM((UnitPrice - UnitCost) * Quantity) AS Total_Profit
FROM Sales;

SELECT
    SUM(Quantity) AS Total_Units_Sold
FROM Sales;

SELECT
    AVG(TotalAmount) AS Average_Order_Value
FROM Sales;

SELECT
    PaymentMethod,
    COUNT(*) AS Number_of_Sales,
    SUM(TotalAmount) AS Revenue
FROM Sales
GROUP BY PaymentMethod
ORDER BY Revenue DESC;

SELECT
    ProductID,
    SUM(Quantity) AS Units_Sold,
    SUM(TotalAmount) AS Revenue
FROM Sales
GROUP BY ProductID
ORDER BY Revenue DESC;

CREATE OR REPLACE VIEW Sales_Analytics AS
SELECT
    s.SaleID,
    s.SaleDateTime,
    s.ProductID,
    p.ProductName,
    s.StoreID,
	st.StoreName,
    st.City,
    s.CustomerID,
    s.Quantity,
    s.PaymentMethod,
    s.UnitPrice,
    s.Discount,
    s.TotalAmount,
    s.UnitCost,
    (s.UnitPrice - s.UnitCost) * s.Quantity AS Profit,
	s.DiscountAmount,
    s.SalesChannel
FROM Sales s
JOIN Products p
ON s.ProductID = p.ProductID
JOIN Stores st
    ON s.StoreID = st.StoreID;

select * from Sales_Analytics;

SELECT
    SaleID,
    UnitPrice,
    Quantity,
    Discount,
    UnitPrice * Quantity * (Discount / 100) AS DiscountAmount
FROM Sales;

ALTER TABLE Sales
ADD COLUMN DiscountAmount DECIMAL(10,2);

UPDATE Sales
SET DiscountAmount = UnitPrice * Quantity * (Discount / 100)
where SaleID > 0;
    
SELECT     
    SaleID,
    UnitPrice,
    Quantity,
    Discount,
    UnitPrice * Quantity * (Discount / 100) AS Test_DiscountAmount
FROM Sales
LIMIT 10;




