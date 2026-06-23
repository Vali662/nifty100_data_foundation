SELECT
    s.broad_sector,
    ROUND(AVG(c.roe_percentage), 2) AS avg_roe
FROM sectors s
JOIN companies c
    ON s.company_id = c.id
WHERE c.roe_percentage IS NOT NULL
GROUP BY s.broad_sector
ORDER BY avg_roe DESC;