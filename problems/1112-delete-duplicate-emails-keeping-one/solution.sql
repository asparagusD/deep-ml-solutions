-- your query
SELECT MIN(id) AS id, email
FROM PERSON
GROUP BY email
ORDER BY id;
