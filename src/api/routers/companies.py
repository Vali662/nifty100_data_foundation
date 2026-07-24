from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


@router.get("/")
def get_companies():
    conn = get_connection()

    query = """
    SELECT
        id,
        company_name
    FROM companies
    ORDER BY company_name;
    """

    companies = conn.execute(query).fetchall()
    conn.close()

    return [dict(row) for row in companies]

@router.get("/{company_id}")
def get_company(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM companies
    WHERE id = ?;
    """

    company = conn.execute(query, (company_id,)).fetchone()

    conn.close()

    if company is None:
        return {
            "error": "Company not found"
        }

    return dict(company)

@router.get("/{company_id}/ratios")
def get_company_ratios(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM financial_ratios
    WHERE company_id = ?
    ORDER BY year DESC;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]

@router.get("/{company_id}/cashflow")
def get_company_cashflow(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM cashflow
    WHERE company_id = ?
    ORDER BY year DESC;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]

@router.get("/{company_id}/balancesheet")
def get_company_balancesheet(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM balancesheet
    WHERE company_id = ?
    ORDER BY year DESC;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]

@router.get("/{company_id}/profitloss")
def get_company_profitloss(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM profitandloss
    WHERE company_id = ?
    ORDER BY year DESC;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]

@router.get("/{company_id}/documents")
def get_company_documents(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM documents
    WHERE company_id = ?
    ORDER BY year DESC;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]

@router.get("/{company_id}/marketcap")
def get_company_marketcap(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM market_cap
    WHERE company_id = ?
    ORDER BY year DESC;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]

@router.get("/{company_id}/peers")
def get_company_peers(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM peer_groups
    WHERE company_id = ?;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]

@router.get("/{company_id}/sector")
def get_company_sector(company_id: str):
    conn = get_connection()

    query = """
    SELECT *
    FROM sectors
    WHERE company_id = ?;
    """

    rows = conn.execute(query, (company_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]