SELECT
    company_name,
    roce_percentage,
    roe_percentage,
    face_value,
    book_value
FROM companies
WHERE roce_percentage IS NOT NULL
ORDER BY roce_percentage DESC
LIMIT 10;