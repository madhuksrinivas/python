# ─────────────────────────────────────────────
# PANDAS 04 — Analysis: groupby, aggregation & reshaping
# ─────────────────────────────────────────────
#
# WHAT IS THIS FILE ABOUT?
#   After cleaning, you need to understand your data.
#   Groupby + aggregation is the pandas equivalent of SQL's
#   GROUP BY — it powers exploratory data analysis (EDA),
#   business dashboards, and feature engineering for ML.
# ─────────────────────────────────────────────

import pandas as pd
import numpy as np

# Sample sales dataset
np.random.seed(42)
n = 200
df = pd.DataFrame({
    "date":     pd.date_range("2026-01-01", periods=n, freq="D"),
    "region":   np.random.choice(["East", "West", "North", "South"], n),
    "product":  np.random.choice(["Widget A", "Widget B", "Gadget X"], n),
    "rep":      np.random.choice([f"Rep{i}" for i in range(1, 8)], n),
    "units":    np.random.randint(10, 200, n),
    "price":    np.random.choice([20.0, 40.0, 150.0], n),
})
df["revenue"] = df["units"] * df["price"]
print(df.head())
print(df.shape)

# ── 1. groupby basics ────────────────────────
# Total revenue per region
print(df.groupby("region")["revenue"].sum())

# Multiple aggregations at once
summary = df.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    avg_units=("units",   "mean"),
    n_orders=("units",    "count"),
    max_revenue=("revenue","max"),
)
print(summary.round(2))

# Aggregation by multiple keys
by_region_product = df.groupby(["region", "product"])["revenue"].sum()
print(by_region_product)
print(by_region_product.unstack())   # pivot to wide format

# ── 2. transform — broadcast group stats back ─
# Useful to add group-level features to each row
df["region_total"]  = df.groupby("region")["revenue"].transform("sum")
df["pct_of_region"] = df["revenue"] / df["region_total"] * 100
print(df[["region", "revenue", "region_total", "pct_of_region"]].head(8))

# Z-score within each group (group normalisation for ML)
df["revenue_zscore"] = (
    df.groupby("product")["revenue"]
    .transform(lambda x: (x - x.mean()) / x.std())
)
print(df[["product", "revenue", "revenue_zscore"]].head(6))

# ── 3. filter — keep groups that meet a condition ─
# Keep only regions with total revenue > 50,000
big_regions = df.groupby("region").filter(lambda g: g["revenue"].sum() > 50_000)
print("Regions kept:", big_regions["region"].unique())

# ── 4. Pivot tables ───────────────────────────
pivot = df.pivot_table(
    values="revenue",
    index="region",
    columns="product",
    aggfunc="sum",
    margins=True,         # add row/col totals
    fill_value=0,
)
print(pivot.round(0))

# ── 5. Merge / join DataFrames ────────────────
products = pd.DataFrame({
    "product":  ["Widget A", "Widget B", "Gadget X"],
    "category": ["hardware", "hardware", "electronics"],
    "cost":     [10.0, 22.0, 80.0],
})

# Inner join — only matching rows
merged = df.merge(products, on="product", how="inner")
merged["profit"] = merged["revenue"] - merged["units"] * merged["cost"]
print(merged[["product", "category", "revenue", "profit"]].head())

# Left join — keep all rows from left, fill non-matching with NaN
reps = pd.DataFrame({"rep": [f"Rep{i}" for i in range(1, 6)],
                     "team": ["A", "A", "B", "B", "C"]})
df2 = df.merge(reps, on="rep", how="left")
print(df2["team"].value_counts(dropna=False))

# ── 6. Time-series features ───────────────────
df["month"]      = df["date"].dt.month
df["week"]       = df["date"].dt.isocalendar().week.astype(int)
df["day_of_week"]= df["date"].dt.dayofweek   # 0=Mon … 6=Sun
df["quarter"]    = df["date"].dt.quarter

# Resample — group by time period (like groupby for dates)
df_ts = df.set_index("date").sort_index()
monthly = df_ts["revenue"].resample("ME").sum()    # month-end
print(monthly)

# Rolling average (7-day) — trend smoothing
rolling = df_ts["revenue"].resample("D").sum().rolling(7).mean()
print(rolling.dropna().head(10))

# ── 7. Value counts, crosstab, correlation ───
print(df["product"].value_counts(normalize=True).round(3))  # proportions

ct = pd.crosstab(df["region"], df["product"], margins=True)
print(ct)

# Correlation matrix — vital for feature selection
numeric = df[["units", "price", "revenue", "pct_of_region"]].corr()
print(numeric.round(2))

# ── 8. Ranking & cumulative stats ─────────────
df["revenue_rank"] = df["revenue"].rank(ascending=False, method="dense")
df["cumulative_rev"] = df.sort_values("date")["revenue"].cumsum()
print(df[["date", "revenue", "revenue_rank", "cumulative_rev"]].head())

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   groupby + agg(named_agg)  — flexible group aggregation
#   transform                 — broadcast group stats to each row
#   pivot_table               — cross-tabulate with margins
#   merge(how="left/inner")   — SQL-style joins
#   resample / rolling        — time-series aggregation
#   .corr()                   — correlation matrix
# ─────────────────────────────────────────────
