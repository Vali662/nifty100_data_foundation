SELECT
    c.company_name,
    m.market_cap_crore,
    m.pe_ratio,
    m.pb_ratio
FROM market_cap m
JOIN companies c
    ON m.company_id = c.id
WHERE m.year = 2024
ORDER BY m.market_cap_crore DESC
LIMIT 20;