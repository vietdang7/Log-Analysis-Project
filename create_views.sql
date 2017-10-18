# Create view errros
CREATE VIEW errors AS
SELECT DATE(log.time) AS day,
CAST(COUNT(log.status) AS FLOAT) AS error_num 
FROM log
WHERE log.status = '404 NOT FOUND'
GROUP BY day;

# Create view total
CREATE VIEW total AS
SELECT DATE(log.time) AS day,
CAST(COUNT(log.status) AS FLOAT) AS total_num 
FROM log
GROUP BY day;
