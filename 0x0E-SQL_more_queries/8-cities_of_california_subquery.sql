-- a script that lists all the cities of california that can be found in the database hbtn_0d_usa
-- You are not allowed to use JOIN statement
SELECT id, name FROM cities WHERE id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
