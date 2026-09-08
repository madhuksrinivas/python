# ─────────────────────────────────────────────
# PANDAS 05 — Feature Engineering & AI Scaling
# ─────────────────────────────────────────────
#
# WHAT IS THIS FILE ABOUT?
#   This file bridges Pandas and machine learning. You will
#   learn how to transform a raw DataFrame into a clean
#   NumPy feature matrix ready for sklearn/PyTorch/TensorFlow,
#   handle large datasets that don't fit in RAM, and apply
#   the Pandas patterns used in production ML pipelines.
# ─────────────────────────────────────────────

import pandas as pd
import numpy as np
import os

# ── 1. Build a realistic ML dataset ──────────
np.random.seed(42)
N = 5_000

df = pd.DataFrame({
    "age":         np.random.randint(18, 70, N),
    "income":      np.random.exponential(50_000, N).astype(int),
    "tenure_months": np.random.randint(1, 120, N),
    "num_products":  np.random.randint(1, 6, N),
    "region":      np.random.choice(["East", "West", "North", "South"], N),
    "plan":        np.random.choice(["basic", "standard", "premium"], N,
                                     p=[0.5, 0.3, 0.2]),
    "last_login_days": np.random.exponential(30, N).astype(int),
    "support_calls": np.random.poisson(2, N),
    "churn":       np.random.choice([0, 1], N, p=[0.8, 0.2]),   # target
})

# Introduce some missing values
for col in ["income", "last_login_days"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

print(df.head())
print(df["churn"].value_counts(normalize=True).round(3))

# ── 2. Numeric feature engineering ───────────

# Log-transform skewed features (reduces effect of extreme values)
df["log_income"]      = np.log1p(df["income"].fillna(df["income"].median()))
df["log_last_login"]  = np.log1p(df["last_login_days"].fillna(0))

# Binning continuous variable into categories (pd.cut)
df["age_group"] = pd.cut(df["age"], bins=[18, 30, 45, 60, 70],
                          labels=["18-30", "31-45", "46-60", "61-70"])

# Quantile-based binning (equal frequency buckets)
df["income_quartile"] = pd.qcut(df["log_income"], q=4,
                                 labels=["Q1", "Q2", "Q3", "Q4"])

# Ratio & interaction features
df["products_per_year"] = df["num_products"] / (df["tenure_months"] / 12 + 1e-3)
df["calls_per_product"] = df["support_calls"] / (df["num_products"] + 1e-3)

# ── 3. Categorical encoding ───────────────────

# Label encoding for ordinal categories
plan_order = {"basic": 0, "standard": 1, "premium": 2}
df["plan_code"] = df["plan"].map(plan_order)

# One-hot encoding for nominal categories
df_encoded = pd.get_dummies(df, columns=["region"], prefix="region", drop_first=False)
print("Columns after one-hot:", [c for c in df_encoded.columns if "region" in c])

# Frequency encoding — replace category with its count (useful for high-cardinality)
freq = df["region"].value_counts(normalize=True)
df["region_freq"] = df["region"].map(freq)

# Target encoding — replace category with mean of target (train only!)
target_mean = df.groupby("region")["churn"].mean()
df["region_target_enc"] = df["region"].map(target_mean)
print(target_mean)

# ── 4. Building the feature matrix X ─────────
feature_cols = [
    "age", "log_income", "tenure_months", "num_products",
    "log_last_login", "support_calls", "plan_code",
    "products_per_year", "calls_per_product",
    "region_freq", "region_target_enc",
]

# One-hot columns added dynamically
region_cols = [c for c in df_encoded.columns if c.startswith("region_")]
feature_cols += region_cols

# Fill any remaining nulls with column median
X = df_encoded[feature_cols].fillna(df_encoded[feature_cols].median())
y = df["churn"].values

print(f"\nFeature matrix: {X.shape}")
print(f"Target:         {y.shape}, positive rate={y.mean():.2%}")

# Convert to NumPy float32 for model training
X_np = X.values.astype(np.float32)
print(f"NumPy array:    {X_np.shape}, dtype={X_np.dtype}")

# ── 5. Train / test split with stratification ─
from sklearn.model_selection import train_test_split  # pip install scikit-learn

try:
    X_train, X_test, y_train, y_test = train_test_split(
        X_np, y, test_size=0.2, stratify=y, random_state=42
    )
    print(f"Train {X_train.shape}, Test {X_test.shape}")
    print(f"Train churn: {y_train.mean():.2%}, Test churn: {y_test.mean():.2%}")
except ImportError:
    print("scikit-learn not installed; skipping split demo")

# ── 6. Memory optimisation for large DataFrames ──
def reduce_mem_usage(df):
    """Downcast numeric columns to smallest sufficient dtype."""
    before = df.memory_usage(deep=True).sum() / 1024**2
    for col in df.select_dtypes(include=["int64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes(include=["float64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="float")
    for col in df.select_dtypes(include=["object"]).columns:
        if df[col].nunique() / len(df) < 0.5:
            df[col] = df[col].astype("category")
    after = df.memory_usage(deep=True).sum() / 1024**2
    print(f"Memory: {before:.2f} MB → {after:.2f} MB  ({100*(before-after)/before:.1f}% saved)")
    return df

df_opt = reduce_mem_usage(df.copy())

# ── 7. Chunked processing for big files ──────
# Simulated large CSV
BIG_CSV = "/tmp/pd_big.csv"
df.to_csv(BIG_CSV, index=False)

results = []
for chunk in pd.read_csv(BIG_CSV, chunksize=1000):
    # Feature engineering on each chunk
    chunk["log_income"] = np.log1p(chunk["income"].fillna(0))
    results.append(chunk["log_income"].mean())

print(f"Mean log_income across chunks: {np.mean(results):.4f}")
os.remove(BIG_CSV)

# ── 8. Exporting the final feature matrix ────
feature_df = pd.DataFrame(X_np, columns=feature_cols)
feature_df["churn"] = y

try:
    feature_df.to_parquet("/tmp/pd_features.parquet", index=False)
    check = pd.read_parquet("/tmp/pd_features.parquet")
    print(f"Parquet saved and reloaded: {check.shape}")
    os.remove("/tmp/pd_features.parquet")
except ImportError:
    feature_df.to_csv("/tmp/pd_features.csv", index=False)
    print("Saved as CSV (install pyarrow for Parquet)")
    os.remove("/tmp/pd_features.csv")

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   np.log1p          — log-transform skewed features
#   pd.cut / pd.qcut  — bin continuous → categorical
#   get_dummies       — one-hot encoding
#   Target encoding   — map category → mean(target)
#   reduce_mem_usage  — downcast dtypes to save RAM
#   Chunked reading   — process files larger than RAM
#   Parquet export    — best format for ML feature stores
#   X.values.astype(np.float32) — hand off to any ML framework
# ─────────────────────────────────────────────
