SELECT MAX(num) as num
FROM MyNumbers
WHERE num in (
    SELECT num
    from MyNumbers
    Group BY num 
    having COUNT(num) = 1
)
