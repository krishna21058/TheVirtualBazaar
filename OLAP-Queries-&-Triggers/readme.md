# OLAP QUERIES

1. OLAP Query to display customer details (for those who bought
products from a particular retailer, for an example store_retailer_id is taken
2 here) using filter of (grouping by) state and their age groups:-

SELECT
IF(GROUPING(c.state), 'All states', c.state) AS Orders_from,
IF(GROUPING(c.age), 'All Age Groups', CONCAT(FLOOR(c.age/10)*10, '-',
FLOOR(c.age/10)*10+9)) AS Age_Group,
COUNT(c.customer_id) AS Number_Of_Orders
FROM final_order AS o
INNER JOIN customer AS c ON c.customer_id = o.order_customer_id
INNER JOIN store AS s ON s.store_product_id = o.order_product_id
WHERE s.store_retailer_id = 2
GROUP BY c.state, c.age WITH ROLLUP;

2. OLAP Query to See the Product Quantity and Product Names of the
Minimum priced products(after discount) in $.

SELECT
IF(GROUPING(p.product_name), 'All Products', p.product_name) AS Product_Name,
ROUND(MIN(p.product_price_in$ *(1-(p.product_discount/100))),2) AS
Min_Cost_After_Discount_in$
FROM product AS p
GROUP BY p.product_name WITH ROLLUP;

3. OLAP Query using GROUPING SETS Alternative to group both product
quantity and names.

SELECT
Product_Quantity, NULL AS Product_name, ROUND(AVG(Product_price_in$),2)
FROM Product
GROUP BY Product_Quantity
UNION ALL
SELECT NULL AS Product_Name, Product_name, ROUND(AVG(Product_price_in$),2)
FROM Product
GROUP BY Product_name;

4. OLAP Query to know the Maximum Products Ordered By their
Categories along with their Category Name and Product Name.

SELECT
IF(GROUPING(c.category_name), 'All Categories', c.category_name) AS Category_Name,
IF(GROUPING(p.product_name), 'All Products', p.product_name) AS Product_Name,
COUNT(o.order_id) AS Number_Of_Orders
FROM final_order AS o
INNER JOIN product AS p ON p.product_id = o.order_product_id
INNER JOIN category AS c ON c.category_id = p.product_category_id
GROUP BY c.category_name, p.product_name WITH ROLLUP;

5. OLAP Query to display the Total Revenue, Group by the Category and
Product.

SELECT
IF(GROUPING(c.category_name), 'All Categories', c.category_name) AS Category,
IF(GROUPING(p.product_name), 'All Categories', p.product_name) AS Product,
ROUND(SUM(o.total_charges),2) AS Total_Revenue
FROM final_order AS o
INNER JOIN store AS s ON s.store_product_id = o.order_product_id
INNER JOIN product AS p ON p.product_id = s.store_product_id
INNER JOIN category AS c ON p.product_category_id = c.category_id
GROUP BY c.category_name,p.product_name WITH ROLLUP;

6. OLAP Query to display the TOP(most ordered) products, categories
using rollup to group by products, categories.

SELECT
IF(GROUPING(c.category_name), 'All Categories', c.category_name) AS
Category_Name,
IF(GROUPING(p.product_name), 'All Products', p.product_name) AS Product_Name,
COUNT(o.order_id) AS Number_Of_Orders
FROM final_order AS o
INNER JOIN product AS p ON p.product_id = o.order_product_id
INNER JOIN category AS c ON c.category_id = p.product_category_id
GROUP BY c.category_name, p.product_name WITH ROLLUP



# Triggers

1. To assign a delivery person(add row to <delivery> table) when
final_order is placed by customer(row is added to <final_order> table).

DELIMITER $
CREATE TRIGGER add_delivery
AFTER INSERT ON final_order
FOR EACH ROW
BEGIN
INSERT INTO delivery (delivery_person_id, delivery_customer_id, delivery_order_id, date)
VALUES ((FLOOR(RAND() * 100) + 1), NEW.order_customer_id, NEW.order_id,
DATE_ADD(NEW.ordered_date, INTERVAL 7 DAY));
END $
DELIMITER ;

2. To decrease quantity of product by 1, whenever a product is added to
cart, by a customer.

DELIMITER $
CREATE TRIGGER dec_quantity
AFTER
INSERT ON Cart
FOR EACH ROW
BEGIN
UPDATE Product SET Product_Quantity = Product_Quantity - NEW.Cart_Product_Quantity
WHERE Product_ID = NEW.Cart_Product_ID;
END $
DELIMITER ;

3. To give an error and not implement insertion into cart, if stock_quantity
is less than quantity asked by customer.

DELIMITER $
CREATE TRIGGER check_stock_quantity
BEFORE
INSERT ON cart
FOR EACH ROW
BEGIN
IF (SELECT product_quantity FROM product WHERE product_id = NEW.cart_product_id) <
NEW.cart_product_quantity THEN
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product out of stock';
END IF;
END $
DELIMITER 