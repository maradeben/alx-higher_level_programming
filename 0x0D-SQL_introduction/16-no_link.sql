-- list all records of table, except those where name has no value
SELECT score, name
FROM `second_table`
WHERE name IS NOT NULL
ORDER BY score DESC
