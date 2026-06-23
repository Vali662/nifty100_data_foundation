SELECT
    s.broad_sector,
    ROUND(AVG(c.roe_percentage), 2) AS avg_roe,
    ROUND(AVG(c.roce_percentage), 2) AS avg_roce,
    COUNT(*) AS company_count
FROM sectors s
JOIN companies c
    ON s.company_id = c.id
GROUP BY s.broad_sector
ORDER BY avg_roce DESC;