SELECT
    company_name,
    roce_percentage,
    roe_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;