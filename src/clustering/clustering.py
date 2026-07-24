import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# -----------------------------------------
# Connect to SQLite Database
# -----------------------------------------

DB_PATH = "data/nifty100.db"

conn = sqlite3.connect(DB_PATH)

print("Connected to database successfully.")

# -----------------------------------------
# Load clustering dataset
# -----------------------------------------

query = """
SELECT
    f.company_id,
    s.broad_sector,
    s.sub_sector,
    f.year,
    f.return_on_equity_pct,
    f.debt_to_equity,
    f.revenue_cagr_5yr,
    f.free_cash_flow,
    f.operating_profit_margin_pct
FROM financial_ratios f
INNER JOIN (
    SELECT
        company_id,
        MAX(year) AS latest_year
    FROM financial_ratios
    GROUP BY company_id
) latest
ON f.company_id = latest.company_id
AND f.year = latest.latest_year
LEFT JOIN sectors s
ON f.company_id = s.company_id;
"""

df = pd.read_sql_query(query, conn)

print("\nDataset Loaded Successfully")
print(df.head())

print("\nDataset Shape:", df.shape)

# -----------------------------------------
# Handle Missing Values
# -----------------------------------------

features = [
    "return_on_equity_pct",
    "debt_to_equity",
    "revenue_cagr_5yr",
    "free_cash_flow",
    "operating_profit_margin_pct"
]

print("\nMissing Values Before Filling:")
print(df[features].isnull().sum())

# Fill missing values with column median
# Fill missing values using Broad Sector median
for col in features:
    df[col] = df.groupby("broad_sector")[col].transform(
        lambda x: x.fillna(x.median())
    )

# Final fallback
df[features] = df[features].fillna(df[features].median())

print("\nMissing Values After Filling:")
print(df[features].isnull().sum())

# -----------------------------------------
# Standardize Features
# -----------------------------------------

scaler = StandardScaler()

X = scaler.fit_transform(df[features])

print("\nFeature Scaling Completed.")
print("Scaled Data Shape:", X.shape)

# -----------------------------------------
# Elbow Method
# -----------------------------------------

wcss = []

for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)
    wcss.append(model.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.grid(True)

plt.savefig("output/elbow_plot.png")
plt.show()

print("\nElbow plot saved to output/elbow_plot.png")
print("Elbow plot saved successfully.")

# -----------------------------------------
# KMeans Clustering
# -----------------------------------------

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X)

cluster_names = {
    0: "Quality Compounders",
    1: "High Growth",
    2: "Turnaround",
    3: "Value Picks",
    4: "Cyclical Leaders"
}

df["cluster_name"] = df["cluster"].map(cluster_names)

print("\nKMeans clustering completed.")
print(df["cluster"].value_counts().sort_index())

print("\nCluster Summary")
print(df["cluster_name"].value_counts())
print("\nCluster vs Broad Sector")
print(pd.crosstab(df["cluster_name"], df["broad_sector"]))

# -----------------------------------------
# Save Cluster Labels
# -----------------------------------------

output_df = df[["company_id", "year", "cluster"]]

output_df = df[
    [
        "company_id",
        "broad_sector",
        "sub_sector",
        "year",
        "cluster",
        "cluster_name"
    ]
]

print("\ncluster_labels.csv saved successfully.")

centers = pd.DataFrame(
    scaler.inverse_transform(kmeans.cluster_centers_),
    columns=features
)

centers["cluster"] = range(5)

centers.to_csv(
    "output/cluster_centers.csv",
    index=False
)

print("cluster_centers.csv saved successfully.")
print("cluster_labels.csv saved successfully.")

conn.close()