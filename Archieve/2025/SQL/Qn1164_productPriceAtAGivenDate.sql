WITH latest as(
    SELECT product_id, MAX(change_date) as change_date
FROM Products
WHERE change_date <= DATE '2019-08-16'
GROUP BY product_id
)

SELECT p.product_id, COALESCE(r.new_price, 10) as price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN latest l ON
    p.product_id = l.product_id
LEFT JOIN Products r
    ON r.product_id = l.product_id 
    AND r.change_date = l.change_date;




