-- View all records
SELECT * FROM sales;

-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM sales;

-- Product-wise Sales
SELECT Product, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product;

-- Region-wise Sales
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region;
SELECT Product, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC;