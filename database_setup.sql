CREATE DATABASE IF NOT EXISTS inventory_portfolio;

USE inventory_portfolio;

CREATE TABLE IF NOT EXISTS item (
    itemid INT AUTO_INCREMENT PRIMARY KEY,
    purchasedate DATE NOT NULL,
    purchaseprice DECIMAL(10, 2) NOT NULL,
    saleprice DECIMAL(10, 2) NULL
);

INSERT INTO item (purchasedate, purchaseprice, saleprice)
VALUES
    ('2026-01-05', 25.00, 40.00),
    ('2026-01-12', 18.50, NULL),
    ('2026-01-20', 35.00, 55.00),
    ('2026-02-03', 42.75, 60.00),
    ('2026-02-14', 15.00, NULL),
    ('2026-02-25', 80.00, 110.00),
    ('2026-03-04', 22.00, 30.00),
    ('2026-03-17', 50.00, NULL),
    ('2026-04-01', 12.50, 20.00),
    ('2026-04-19', 65.00, 90.00),
    ('2026-05-07', 28.00, NULL),
    ('2026-05-22', 100.00, 145.00),
    ('2026-06-10', 45.00, 38.00),
    ('2026-07-02', 33.50, NULL),
    ('2026-08-15', 55.00, 75.00);

SELECT COUNT(*) AS total_items
FROM item;

SELECT * FROM item;