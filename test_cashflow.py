from src.analytics.cashflow_kpis import free_cash_flow
from src.analytics.cashflow_kpis import cfo_quality_score
from src.analytics.cashflow_kpis import capex_intensity
from src.analytics.cashflow_kpis import fcf_conversion_rate
from src.analytics.cashflow_kpis import capital_allocation_pattern

print("Free Cash Flow")

print(
    free_cash_flow(
        500,
        -200
    )
)

print(
    free_cash_flow(
        200,
        -500
    )
)

print(
    free_cash_flow(
        -100,
        -300
    )
)
print("\nCFO Quality Score")

print(cfo_quality_score(120, 100))

print(cfo_quality_score(70, 100))

print(cfo_quality_score(30, 100))

print(cfo_quality_score(100, 0))

print("\nCapEx Intensity")

print(capex_intensity(-20, 1000))

print(capex_intensity(-50, 1000))

print(capex_intensity(-150, 1000))

print(capex_intensity(-50, 0))

print("\nFCF Conversion Rate")

print(
    fcf_conversion_rate(
        300,
        500
    )
)

print(
    fcf_conversion_rate(
        -200,
        400
    )
)

print(
    fcf_conversion_rate(
        300,
        0
    )
)
print("\nCapital Allocation Pattern")

print(capital_allocation_pattern(500, -200, -100))

print(capital_allocation_pattern(500, 100, -50))

print(capital_allocation_pattern(-100, 200, 300))

print(capital_allocation_pattern(-100, -200, 300))

print(capital_allocation_pattern(100, 200, 300))

print(capital_allocation_pattern(-100, -200, -300))

print(capital_allocation_pattern(100, -200, 300))