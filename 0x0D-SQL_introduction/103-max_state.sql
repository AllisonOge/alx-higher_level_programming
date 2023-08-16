-- script that displays the max temperature according to state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
