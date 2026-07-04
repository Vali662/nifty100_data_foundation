from src.analytics.cagr import (
    calculate_cagr,
    revenue_cagr,
    pat_cagr,
    eps_cagr,
)

print("Revenue CAGR")
print(revenue_cagr(100, 200, 5))

print("\nPAT CAGR")
print(pat_cagr(50, 100, 5))

print("\nEPS CAGR")
print(eps_cagr(10, 20, 5))