SELECT
    s.broad_sector,
    ROUND(AVG(c.roce_percentage), 2) AS avg_roce
FROM sectors s
JOIN companies c
    ON s.company_id = c.id
WHERE c.roce_percentage IS NOT NULL
GROUP BY s.broad_sector
ORDER BY avg_roce DESC;