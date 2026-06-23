SELECT
    (SELECT COUNT(*) FROM companies) AS total_companies,

    (SELECT COUNT(DISTINCT broad_sector)
     FROM sectors) AS total_sectors,

    (SELECT company_name
     FROM companies
     ORDER BY roe_percentage DESC
     LIMIT 1) AS top_roe_company,

    (SELECT company_name
     FROM companies
     ORDER BY roce_percentage DESC
     LIMIT 1) AS top_roce_company;