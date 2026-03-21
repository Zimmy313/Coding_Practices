--------- more efficient. using SUM(state = 'approved)
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY country, month
ORDER BY month, country;


WITH approved_transactions AS (
    SELECT 
        country, 
        DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        COUNT(*) AS approved_count, 
        SUM(amount) AS approved_total_amount
    FROM Transactions
    WHERE state = 'approved'
    GROUP BY country, month
),
all_transactions AS (
    SELECT 
        country, 
        DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        COUNT(*) AS trans_count, 
        SUM(amount) AS trans_total_amount
    FROM Transactions
    GROUP BY country, month
)

SELECT 
    at.month,
    at.country,
    at.trans_count,
    IFNULL(ap.approved_count, 0) AS approved_count,
    at.trans_total_amount,
    IFNULL(ap.approved_total_amount, 0) AS approved_total_amount
FROM all_transactions at
LEFT JOIN approved_transactions ap
    ON (at.country <=> ap.country)  AND at.month = ap.month
ORDER BY at.month, at.country;
