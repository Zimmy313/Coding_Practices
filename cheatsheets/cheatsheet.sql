/*
=============================================================
MySQL Common Functions Cheat Sheet
=============================================================
*/

-- =====================================
-- General Utilities (MySQL) - Templates
-- =====================================

SELECT
  -- NULL handling
  COALESCE(arg1, arg2, arg3, ...)     AS coalesce_first_non_null, -- returns first non-NULL
  IFNULL(expr, alt_value)             AS ifnull_mysql_only,       -- 2 args: if expr is NULL, return alt_value
  NULLIF(expr1, expr2)                AS nullif_equal_to_null,    -- if expr1 = expr2 -> NULL, else expr1

  -- Conditional logic
  IF(condition, true_value, false_value)  AS if_expr,             -- 3 args
  CASE 
      WHEN condition1 THEN result1
      WHEN condition2 THEN result2
      ELSE default_result
  END AS case_expr,

  -- Safe division
  num / NULLIF(den, 0)                AS safe_divide,             -- avoids divide by zero

  -- NULL-safe comparison
  (expr1 <=> expr2)                   AS null_safe_equal,         -- true if equal OR both NULL

  -- Casting
  CAST(expr AS target_type)           AS cast_expr,               -- e.g. CAST('123' AS UNSIGNED)
  CONVERT(expr, type)                 AS convert_expr,            -- or CONVERT(expr USING charset)

  -- String length
  LENGTH(str)                         AS byte_len,                -- bytes
  CHAR_LENGTH(str)                    AS char_len,                -- characters

  -- Regex (MySQL 8+)
  REGEXP_LIKE(str, pattern)           AS re_match,                -- true/false
  REGEXP_REPLACE(str, pattern, repl)  AS re_replace,              -- replace match with repl
  REGEXP_SUBSTR(str, pattern, start_occurrence, nth) AS re_sub,   -- extract nth match

  -- Aggregates
  COUNT(*)                            AS total_rows,              -- number of rows
  COUNT(DISTINCT col)                 AS uniq_count,
  SUM(condition)                      AS condition_true_count,    -- count of rows matching condition

  -- List aggregation
  GROUP_CONCAT(expr ORDER BY expr SEPARATOR ',') AS csv_list;


-- =====================================
-- String Functions
-- =====================================
SELECT 
    LENGTH('LeetCode') AS str_length,       -- String length -> 8
    LOWER('LeetCode') AS lower_case,        -- Lowercase -> 'leetcode'
    UPPER('LeetCode') AS upper_case,        -- Uppercase -> 'LEETCODE'
    TRIM('   abc   ') AS trimmed,           -- Remove leading & trailing spaces
    LTRIM('   abc') AS left_trim,           -- Remove leading spaces
    RTRIM('abc   ') AS right_trim,          -- Remove trailing spaces
    CONCAT('Leet', 'Code') AS combined,     -- Concatenate strings
    CONCAT_WS('-', '2025', '09', '24') AS concat_with_sep, -- -> '2025-09-24'
    LEFT('LeetCode', 4) AS left_substring,  -- First 4 characters -> 'Leet'
    RIGHT('LeetCode', 4) AS right_substring,-- Last 4 characters -> 'Code'
    SUBSTRING('LeetCode', 2, 4) AS sub_str, -- From index 2, length 4 -> 'eetC'
    REPLACE('leet code', ' ', '_') AS replaced, -- Replace space with underscore
    LOCATE('Code', 'LeetCode') AS found_at, -- Position of substring -> 5
    REVERSE('abc') AS reversed;             -- Reverse string -> 'cba'

-- =====================================
-- Numeric / Math Functions
-- =====================================
SELECT 
    ABS(-10) AS abs_val,            -- Absolute value -> 10
    ROUND(3.14159, 2) AS rounded,   -- Round to 2 decimal places -> 3.14
    CEIL(2.3) AS ceil_val,          -- Ceiling -> 3
    FLOOR(2.9) AS floor_val,        -- Floor -> 2
    POW(2, 3) AS power_val,         -- Power -> 8
    SQRT(16) AS sqrt_val,           -- Square root -> 4
    GREATEST(10, 20, 30) AS max_val,-- Max of multiple values -> 30
    LEAST(10, 20, 30) AS min_val,   -- Min of multiple values -> 10
    MOD(10, 3) AS mod_val,          -- Remainder -> 1
    RAND() AS random_num;           -- Random number between 0 and 1

-- =====================================
-- Aggregate Functions
-- =====================================
SELECT 
    COUNT(*) AS total_rows,        -- Count rows
    SUM(salary) AS total_salary,   -- Sum of a column
    AVG(salary) AS avg_salary,     -- Average value
    MIN(salary) AS min_salary,     -- Minimum value
    MAX(salary) AS max_salary;     -- Maximum value

-- =====================================
-- Conditional / Logical Functions
-- =====================================
SELECT 
    IF(10 > 5, 'YES', 'NO') AS if_result,       -- If condition
    IFNULL(NULL, 'default_value') AS ifnull_res,-- Replace NULL with default
    COALESCE(NULL, NULL, 'first_non_null') AS coalesce_res, -- First non-null
    CASE 
        WHEN score >= 90 THEN 'A'
        WHEN score >= 80 THEN 'B'
        ELSE 'C'
    END AS grade
FROM students;

-- =====================================
-- Window Functions 
-- =====================================
SELECT 
    id,
    score,
    ROW_NUMBER() OVER (PARTITION BY class ORDER BY score DESC) AS row_num,
    RANK() OVER (PARTITION BY class ORDER BY score DESC) AS rank_num,
    DENSE_RANK() OVER (PARTITION BY class ORDER BY score DESC) AS dense_rank_num,
    NTILE(4) OVER (ORDER BY score DESC) AS quartile_group,
    SUM(score) OVER (PARTITION BY class) AS class_total
FROM students;

/*
Template for Window Functions:
<function>() OVER (
    PARTITION BY <columns>     -- Optional: Grouping scope
    ORDER BY <columns>         -- Required for ranking / sequencing
    ROWS BETWEEN <frame>       -- Optional: Default depends on function
);
*/


-- =====================================
-- Date and Time Functions (MySQL)
-- =====================================
-- Types:
--   DATE        -> 'YYYY-MM-DD'
--   TIME        -> 'HH:MM:SS'
--   DATETIME    -> local-wall time; no TZ conversion
--   TIMESTAMP   -> stored in UTC; converted to @@time_zone on read
-- Prefer ISO literals: '2025-09-24' and '2025-09-24 13:45:00'
-- =====================================

-- GETTING "NOW", PARTS, FORMATTING
SELECT
  NOW()                              AS current_timestamp,   -- DATETIME
  CURDATE()                          AS current_date,        -- DATE
  CURTIME()                          AS current_time,        -- TIME
  EXTRACT(YEAR  FROM NOW())          AS yr,                  -- standard extractor
  EXTRACT(MONTH FROM NOW())          AS mon,
  EXTRACT(DAY   FROM NOW())          AS day,
  EXTRACT(HOUR  FROM NOW())          AS hr,
  EXTRACT(MINUTE FROM NOW())         AS min,
  EXTRACT(SECOND FROM NOW())         AS sec,
  DAYNAME(NOW())                     AS day_name,            -- e.g. 'Wednesday'
  WEEKDAY(NOW())                     AS weekday_num,         -- 0=Monday
  DATE_FORMAT(NOW(), '%Y-%m-%d')     AS fmt_ymd,             -- formatting to string
  DATE(NOW())                        AS truncated_date;      -- drop time part

-- ADD/SUBTRACT INTERVALS
SELECT
  DATE_ADD('2025-09-24', INTERVAL 7 DAY)      AS plus_7d,
  DATE_SUB('2025-09-24', INTERVAL 1 MONTH)    AS minus_1m,
  TIMESTAMPADD(HOUR, 36, '2025-09-24 12:00')  AS plus_36h,
  TIMESTAMPDIFF(DAY,
    '2025-09-01', '2025-09-24')               AS diff_days,  -- precise diff in days
  DATEDIFF('2025-09-24', '2025-09-01')        AS datediff_days; -- alias, same purpose

-- PARSING & STRING FORMATTING
SELECT
  STR_TO_DATE('24/09/2025', '%d/%m/%Y')       AS parsed_ddmmyyyy,
  DATE_FORMAT('2025-09-24', '%a, %b %e')      AS human_short;  -- "Wed, Sep 24"
-- Note: DATE_FORMAT always returns a string

-- TRUNCATING TO PERIODS (month start/end)
SELECT
  DATE_FORMAT(NOW(), '%Y-%m-01')                       AS month_start,   -- first day of month
  DATE_ADD(DATE_FORMAT(NOW(), '%Y-%m-01'), INTERVAL 1 MONTH) AS next_month_start,
  LAST_DAY(NOW())                                      AS month_end;

-- EXTRA: WEEK / QUARTER HELPERS
SELECT
  WEEK(NOW(), 3)      AS iso_week,     -- mode=3 => ISO week number
  QUARTER(NOW())      AS quarter_num;  -- 1-4
