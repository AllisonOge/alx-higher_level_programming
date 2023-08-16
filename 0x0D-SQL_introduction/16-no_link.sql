-- a script that lists all records of the table second_table while ignoring records without name
-- records should display the score and the name (in this order) in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name!="" ORDER BY score DESC;
